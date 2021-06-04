"""Module for Follower class, by Marc Howard and Miriam Melnick."""
class Follower(object):
    """Follower class tracks the distance to objects and attempts to follow the closest object."""

    def __init__(self, driver, distance_sensor, follow_distance_mm, follower_pid):
        self.driver = driver
        self.distance_sensor = distance_sensor
        self.follow_distance = follow_distance_mm
        self.pid = follower_pid

        self.reverse_distance_mm = 100
        self.stop_distance_mm = 300
        self.move_towards_distance_mm = 1500

    def step(self):
        """Advance the goal one step."""
        distance_reading = self.distance_sensor.distanceUSEV3()
        print "Follower: sensing something at distance {0}".format(distance_reading)
        error = distance_reading - self.follow_distance
        speed = self.pid.calculate_response(error)

        if distance_reading < self.reverse_distance_mm:
            print "Follower: telling driver to stop"
            self.driver.stop()
        elif distance_reading < self.stop_distance_mm:
            print "Follower: telling driver to move backwards at speed {0}".format(speed)
            self.driver.go_backwards(speed)
        elif distance_reading < self.move_towards_distance_mm:
            print "Follower: telling driver to move straight at speed {0}".format(speed)
            self.driver.go_straight(speed)
        else:
            print "Follower: turning left at speed 50"
            self.driver.turn_left(50)

        self.driver.step()
