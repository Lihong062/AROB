import math

class Marker(object):
    def __init__(self, heading, x, y, marker_id):
        self.heading = heading
        self.x = x
        self.y = y
        self.marker_id = marker_id
    def __repr__(self):
        return "Marker {} at ({}, {}) and heading {}".format(
            self.marker_id, self.x, self.y, self.heading)


class TriangulationTracker(object):
    """Use triangulation based on ArUco markers to determine robot location."""
    def __init__(self, driver, gyro_sensor, jevois_handler, triangulation_calculator):
        self.driver = driver
        self.gyro_sensor = gyro_sensor
        self.jevois_handler = jevois_handler
        self.triangulation_calculator = triangulation_calculator

        self.center_threshold = 50
        self.initial_heading = self.gyro_sensor.gyroAngleEV3()
        self.currently_gathering_data = False
        self.marker_locations = {"U14": [1000, 870],
                                 "U16": [2000, 870],
                                 "U17": [1500, -870]}
        self.markers = {"U14": None,
                        "U16": None,
                        "U17": None}
        self.x_robot = 0
        self.y_robot = 0

    def step(self):
        # If data collection is in progress, keep working on it. Else, pass.
        if not self.currently_gathering_data:
            return

        heading = self.get_heading()
        objects = self.jevois_handler.getObjects()

        # Make a list of all JevoisObjects we fetched that represent ArUco codes
        codes = [obj for obj in objects if obj.object_id[0] == 'U']
        for code in codes:
            aruco_id = code.object_id
            # If the code is close to the center of our screen
            # and we have not already saved this marker...
            if abs(code.x_coord) < self.center_threshold and not self.markers[aruco_id]:
                # Save the heading for the appropriate ArUco code.
                self.markers[aruco_id] = Marker(heading,
                                                self.marker_locations[aruco_id][0],
                                                self.marker_locations[aruco_id][1],
                                                aruco_id)
                print "Saved heading {} for code {}".format(heading, code.object_id)
        # print markers  # Uncomment this to see what markers it's found so far
        if self.markers["U14"] and self.markers["U16"] and self.markers["U17"]:
            self._conclude_data_collection()

        # Since we're still collecting data, keep turning left slowly.
        self.driver.turn_left(10)
        self.driver.step()

    def begin_data_collection(self):
        """Prep for data collection, doing internal bookkeeping only."""
        self.markers = {"U14": None,
                        "U16": None,
                        "U17": None}
        self.currently_gathering_data = True

    def is_data_collection_ongoing(self):
        """Return a boolean, whether data collection is in progress."""
        return self.currently_gathering_data

    def get_last_location(self):
        """Return the last recorded location. This is fast!"""
        return [self.x_robot, self.y_robot]

    def get_heading(self):
        """Return heading in degrees. This should be stored internally."""
        gyro_diff = self.gyro_sensor.gyroAngleEV3() - self.initial_heading
        return (gyro_diff * -1) % 360

    def _conclude_data_collection(self):
        """Finish the data collection, calculating and storing the x and y of the robot."""
        print "done collecting data - calculating estimates"
        estimate1 = self.triangulation_calculator.findRobotGivenTwoMarkers(self.markers["U14"], self.markers["U16"])
        estimate2 = self.triangulation_calculator.findRobotGivenTwoMarkers(self.markers["U16"], self.markers["U17"])
        estimate3 = self.triangulation_calculator.findRobotGivenTwoMarkers(self.markers["U14"], self.markers["U17"])
        location = self.triangulation_calculator.findAverageOfClosestTwoEstimates(estimate1, estimate2, estimate3)
        print "estimates: ", [estimate1, estimate2, estimate3]
        self.x_robot = location[0]
        self.y_robot = location[1]
        self.currently_gathering_data = False


class TriangulationCalculator(object):
    """Helper class to do triangulation calculations."""

    def findRobotGivenTwoMarkers(self, marker1, marker2):
        """Given two markers, estimate the robot's location."""
        x1 = marker1.x
        y1 = marker1.y
        tan_1 = self.tan(marker1.heading)
        x2 = marker2.x
        y2 = marker2.y
        tan_2 = self.tan(marker2.heading)
        x_robot = (x2*tan_2 - y2 + y1 - x1 * tan_1) / (tan_2 - tan_1)
        y_robot = y1 - tan_1*(x1 - x_robot)
        return [x_robot, y_robot]

    def findAverageOfClosestTwoEstimates(self, estimate1, estimate2, estimate3):
        """Given 3 robot location estimates, ignore the worst, and average the others."""
        diff_1_2 = self._findDistanceBetweenTwoPoints(estimate1, estimate2)
        diff_2_3 = self._findDistanceBetweenTwoPoints(estimate2, estimate3)
        diff_1_3 = self._findDistanceBetweenTwoPoints(estimate1, estimate3)
        diff_list = [diff_1_2, diff_2_3, diff_1_3]

        if diff_1_2 == min(diff_list):
            return self._getAverageOfTwoPoints(estimate1, estimate2)
        elif diff_2_3 == min(diff_list):
            return self._getAverageOfTwoPoints(estimate2, estimate3)
        else:
            return self._getAverageOfTwoPoints(estimate1, estimate3)

    def _findDistanceBetweenTwoPoints(self, point1, point2):
        x_diff = point1[0] - point2[0]
        y_diff = point1[1] - point2[1]
        return math.sqrt(x_diff ** 2 + y_diff ** 2)

    def _getAverageOfTwoPoints(self, point1, point2):
        x = (point1[0] + point2[0]) / 2
        y = (point1[1] + point2[1]) / 2
        return [x, y]

    def tan(self, angle_in_degrees):
        return math.tan(math.radians(angle_in_degrees))