"""Main code that runs a follower program."""
import time
from PiStorms import PiStorms
from driver import Driver
from dead_reckoning_tracker import DeadReckoningTracker
from mapper import Mapper
from pid_controller import PIDController
from block_navigator import BlockNavigator
from jevois_handler import JevoisHandler
psm = PiStorms()

left_motor = psm.BAM1
right_motor = psm.BAM2
distance_sensor = psm.BAS1
gyro_sensor = psm.BAS2
mms_moved_per_motor_degree = 135.02/360

driver = Driver(left_motor, right_motor, motors_mounted_backwards=True)
turn_pid = PIDController(1, 0, 0.0001)
straight_pid = PIDController(.2, 0, 0.0001)
dead_reckoning_tracker = DeadReckoningTracker(gyro_sensor, left_motor, right_motor, mms_moved_per_motor_degree)
mapper = Mapper(psm)
jevois_handler = JevoisHandler()
block_navigator = BlockNavigator(driver, turn_pid)

while not psm.isKeyPressed():
    dead_reckoning_tracker.update_position_and_heading()
    current_location = dead_reckoning_tracker.get_location()
    mapper.add_robot_location(current_location)
    blocks = jevois_handler.getObjects()
    if len(blocks) > 0:
        block_navigator.step_toward_block(blocks[0])
    time.sleep(.05)

left_motor.brake()
right_motor.brake()
mapper.plot()