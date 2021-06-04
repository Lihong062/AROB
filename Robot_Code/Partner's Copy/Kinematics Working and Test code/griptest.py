from PiStorms import PiStorms
from gripper_class import Gripper
import time
psm =                       PiStorms()
gripper_motor =             psm.BAM1

gripper = Gripper(gripper_motor)



gripper.grip()

time.sleep(5)
gripper.release()