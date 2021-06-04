class PathNavigator(object):
    """PathNavigator moves the robot through a series of points."""
    def __init__(self, point_navigator, acceptable_error_mms):
    def append_new_point_to_path(self, point):
    def set_path(self, path):
    def step(self):

class PointNavigator(object):
    """PointNavigator moves the robot to a given point, and then stops."""
    def __init__(self, dead_reckoning_tracker, driver, turn_pid, straight_pid):
    def set_point_goal(self, point_goal):
    def get_distance_to_goal(self):
    def step(self):
    def _update_distance_and_heading_to_goal(self): # Recommended optional private function

class Mapper(object):
    """Mapper class keeps track locations discovered and travelled by the robot."""
    def __init__(self, psm):
    def add_robot_location(self, location):
    def plot(self):

class DeadReckoningTracker(object):
    """DeadReckoningTracker class tracks robot position and heading using gyro and servos."""
    def __init__(self, gyro_sensor, left_motor, right_motor, mms_moved_per_motor_degree, motors_mounted_backwards=False):
    def update_position_and_heading(self):
    def get_location(self):
    def get_heading(self):

class PIDController(object):
    """PID calculates appropriate response to smoothly achieve a goal."""
    def __init__(self, Kp, Ki, Kd):
    def calculate_response(self, error):

class Follower(object):
    """Follower can follow a person at a preset distance."""
    def __init__(self, driver, distance_sensor, follow_distance_mm, follower_pid):
    def step(self):

class Driver(object):
    """Driver class can move a robot with a certain direction goal and speed goal."""
    def __init__(self, left_motor, right_motor, motors_mounted_backwards=False):
    # These functions change the goal
    def stop(self):
    def go_straight(self, speed):
    def turn_right(self, speed):
    def turn_left(self, speed):
    def go_backwards(self, speed):
    # This function advances the goal
    def step(self):
    # Optional, but recommended private helper functions
    def _safety_cap_speed(self, speed):

