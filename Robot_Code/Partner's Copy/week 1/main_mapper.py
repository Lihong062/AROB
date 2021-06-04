"""Main code that runs a follower program."""
import time
from PiStorms import PiStorms
from final_driver import Driver
from final_follower import Follower
from final_dead_reckoning_tracker import DeadReckoningTracker
from final_pid_controller import PIDController
from mapper import Mapper
psm = PiStorms()

left_motor = psm.BAM1
right_motor = psm.BAM2
distance_sensor = psm.BAS1
gyro_sensor = psm.BAS2
mms_moved_per_motor_degree = 1

driver = Driver(left_motor, right_motor, motors_mounted_backwards=True)
pid = PIDController(1, 0, 0.0001)
follower = Follower(driver, distance_sensor, follow_distance_mm=300, follower_pid=pid)
dead_reckoning_tracker = DeadReckoningTracker(gyro_sensor, left_motor, right_motor, mms_moved_per_motor_degree)
mapper = Mapper(psm)

while not psm.isKeyPressed():
    follower.step()
    dead_reckoning_tracker.update_position_and_heading()
    current_location = dead_reckoning_tracker.get_location()
    psm.screen.termPrintAt(1, "Location: {}, {}".format(current_location[0], current_location[1]))
    mapper.add_robot_location(current_location)
    time.sleep(.05)

left_motor.brake()
right_motor.brake()
mapper.plot()