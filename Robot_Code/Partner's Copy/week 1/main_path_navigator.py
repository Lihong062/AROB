"""Main code that runs a follower program."""
import time
from PiStorms import PiStorms
from driver import Driver
from path_navigator import PathNavigator
from point_navigator import PointNavigator
from pid_controller import PIDController
from dead_reckoning_tracker import DeadReckoningTracker
from mapper import Mapper
psm = PiStorms()

left_motor = psm.BAM2
right_motor = psm.BAM1
distance_sensor = psm.BAS1
gyro_sensor = psm.BAS2
mms_moved_per_motor_degree = 135.65/360

driver = Driver(left_motor, right_motor, motors_mounted_backwards=True)
straight_pid = PIDController(1, 0.0001, 0.0001)
turn_pid = PIDController(0.5, 0.0001, 0.0001)
dead_reckoning_tracker = DeadReckoningTracker(
    gyro_sensor, left_motor, right_motor, mms_moved_per_motor_degree, motors_mounted_backwards=True)
mapper = Mapper(psm)
point_navigator = PointNavigator(dead_reckoning_tracker, driver, turn_pid, straight_pid)
path_navigator = PathNavigator(point_navigator, 50)

path = [[500, 500], [500, -500], [0, 0]]
path_navigator.set_path(path)
while not psm.isKeyPressed() and not path_navigator.is_path_completed():
    path_navigator.step()
    current_location = dead_reckoning_tracker.get_location()
    psm.screen.termPrintAt(1, "Location: {}, {}".format(
        int(current_location[0]), int(current_location[1])))
    current_goal = path_navigator.path[path_navigator.current_goal_path_index]
    psm.screen.termPrintAt(3, "Goal: {}, {}".format(int(current_goal[0]), int(current_goal[1])))
    mapper.add_robot_location(current_location)

left_motor.brake()
right_motor.brake()
mapper.plot()