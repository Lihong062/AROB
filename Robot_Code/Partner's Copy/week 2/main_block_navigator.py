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
right_motor = psm.BBM2
distance_sensor = psm.BAS1
gyro_sensor = psm.BAS2
mms_moved_per_motor_degree = 135.02/360  # Replace with your own wheel size

driver = Driver(left_motor, right_motor, motors_mounted_backwards=False)
turn_pid = PIDController(.01, 0, 0.0001)
dead_reckoning_tracker = DeadReckoningTracker(gyro_sensor, left_motor, right_motor, mms_moved_per_motor_degree)
mapper = Mapper(psm)
jevois_handler = JevoisHandler()
block_navigator = BlockNavigator(driver, turn_pid)

def first_blob(blocks):
    """Return the first object that is a blob (not ArUco), or None."""
    for block in blocks:
        if "blob" in block.object_id:
            return block
    return None

# Keep looping until we reach the block or hit the kill switch
while not psm.isKeyPressed() and not block_navigator.check_if_at_block():
    dead_reckoning_tracker.update_position_and_heading()
    current_location = dead_reckoning_tracker.get_location()
    mapper.add_robot_location(current_location)
    blocks = jevois_handler.getObjects()
    if len(blocks) > 0:
        block = first_blob(blocks)
        if block is not None:
            block_navigator.step_toward_block(block)
    time.sleep(.05)

left_motor.brake()
right_motor.brake()
mapper.plot()