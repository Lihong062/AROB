class Joint(object):
    """Simple class to clearly store joint information."""
    def __init__(self, x_length_in_mm, y_length_in_mm, angle_in_degrees):

class JointMotor(object):
    """A wrapper for motor that can keep it at a certain position."""
    def __init__(self, motor, pid=None):
    def set_goal_position(self, position):
        """Set the goal position of the motor."""
    def step(self):
        """Take a step towards having the motor in the right position."""

class ForwardKinematics(object):
    """Calculates the endpoint of a gripper, given a series of joints."""
    def calculateGripperPosition(self, joints):
        """Do the calculations, and return P0 (gripper position in standard coordinate plane)"""
    def _shift_reference_frame_K_to_K_minus_1(self, position_K, theta_K, x_K_minus_1, y_K_minus_1):
        """Shift reference frame from K+1 to K by calculating the rotation and translation matrices required."""

class InverseKinematics(object):
    """Calculate the joint angles required to achieve a gripper position."""
    def __init__(self, forward_kinematics, margin_of_error):
    def calculateJointAngles(self, desired_gripper_position, joints):
        """Produce a list of joint angles to produce a desired gripper location."""
    def _are_joint_angles_valid(self, joint_angles):
        """Return True if this set of angles is safe for your arm, else False"""

class BlockLocator(object):
    """Navigates a path and records the location of blocks along its path."""
    def __init__(self, path_navigator, block_navigator, pixy_handler, mapper):
    def step(self):

class BlockNavigator(object):
    """Navigates to a specific block and stops when it arrives."""
    def __init__(self, driver):
    def stepTowardBlock(self, block):
    def checkIfAtBlock(self, block):

class Marker(object):
    def __init__(self, heading, x, y, marker_id):

class TriangulationTracker(object):
"""Use triangulation based on ArUco markers to determine robot location."""
    def __init__(self, driver, gyro_sensor, jevois_handler, triangulation_calculator):
    def step(self):
    def begin_data_collection(self):
    def is_data_collection_ongoing(self):
    def get_last_location(self):
    def get_heading(self):

class TriangulationCalculator(object):
    def findRobotGivenTwoMarkers(self, marker1, marker2):
    def findAverageOfClosestTwoEstimates(self, estimate1, estimate2, estimate3):

class Mapper(object):
    """Mapper class keeps track of a robot's current location and previous path."""
    def __init__(self, left_motor, right_motor, gyro_sensor, psm, camera, motors_mounted_backwards=False):
    def step(self):  # This now uses SLAM to update a 2D map at every step
    def plot(self, points_to_plot):  # Plots path traveled and the map of the environment
    def getLocation(self):
    def getHeading(self):
    def canIGoToPoint(self, point): # Tells us if a point is reachable given current map
    def getPathBetweenTwoPoints(self, point1, point1):  # Returns path given 2D map, or None if no known path

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

