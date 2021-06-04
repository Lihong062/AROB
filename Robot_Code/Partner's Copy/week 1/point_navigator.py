"""Module for PointNavigator class, by Marc Howard and Miriam Melnick"""
import math
class PointNavigator(object):
    """PointNavigator moves the robot to a given point, and then stops."""
    def __init__(self, dead_reckoning_tracker, driver, turn_pid, straight_pid):
        self.dead_reckoning_tracker = dead_reckoning_tracker
        self.driver = driver
        self.turn_pid = turn_pid
        self.straight_pid = straight_pid

        self.point_goal = []
        self.distance_to_goal = 0
        self.heading_to_goal = 0
        self.heading_diff = 0

    def set_point_goal(self, point_goal):
        """Change the goal."""
        self.point_goal = point_goal

    def get_distance_to_goal(self):
        """Get updated distance to goal."""
        self._update_distance_and_heading_to_goal()
        return self.distance_to_goal

    def step(self):
        """Take a step towards the goal."""
        self.dead_reckoning_tracker.update_position_and_heading()
        self._update_distance_and_heading_to_goal()

        turning_speed = abs(self.turn_pid.calculate_response(self.heading_diff))
        forward_speed = self.straight_pid.calculate_response(self.distance_to_goal)
        if self.heading_diff > 10:
            print 'PointNavigator: heading is way off - turning left'
            self.driver.turn_left(turning_speed)
        elif self.heading_diff < -10:
            print 'PointNavigator: heading is way off - turning right'
            self.driver.turn_right(turning_speed)
        else:
            print 'PointNavigator: close to on target - going straight'
            self.driver.go_straight(forward_speed)
        self.driver.step()

    def _update_distance_and_heading_to_goal(self):
        """Calculate an updated differential to the goal."""
        location = self.dead_reckoning_tracker.get_location()
        heading = self.dead_reckoning_tracker.get_heading()

        x_diff_to_target = self.point_goal[0] - location[0]
        y_diff_to_target = self.point_goal[1] - location[1]
        self.distance_to_goal = (math.sqrt(math.pow(x_diff_to_target, 2) +
                                           math.pow(y_diff_to_target, 2)))

        self.heading_to_goal = math.degrees(math.atan2(y_diff_to_target, x_diff_to_target))
        self.heading_diff = ((self.heading_to_goal - heading + 180) % 360) - 180
        # print "PointNavigator: I am at {}, {}. I want to be at {}, {}.".format(
        #     location[0], location[1], self.point_goal[0], self.point_goal[1])
        # msg = "PointNavigator: I am trying to go to heading {} so I need to turn {} to get there"
        # print msg.format(self.heading_to_goal, self.heading_diff)
