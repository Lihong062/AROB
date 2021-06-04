from PiStorms                                   import PiStorms
import math
import time
import numpy as np
import matplotlib.pyplot as plt
from kinematics_class_wc_pick_it_up             import Joint
from kinematics_class_wc_pick_it_up             import JointMotor
from kinematics_class_wc_pick_it_up             import ForwardKinematics
from inverse_kinematics_class_wc_pick_it_up     import InverseKinematics
from gripper_class                              import Gripper
from driver                                     import Driver
from jevois_handler                             import JevoisHandler
from block_navigator                            import BlockNavigator
from dead_reckoning_tracker                     import DeadReckoningTracker
from path_navigator                             import PathNavigator
from point_navigator                            import PointNavigator
from pid_controller                             import PIDController
from mapper                                     import Mapper
from robo_arm_class                             import PickerUpper
from person_checker_class                       import PersonChecker

psm =                       PiStorms()

left_motor =                psm.motor1
right_motor =               psm.motor2

joint_1_motor =             psm.motor3
joint_2_motor =             psm.motor4
gripper_motor =             psm.motor5

gyro =                      psm.sensor1

driver =                    Driver(left_motor, right_motor, True)
straight_pid =              PIDController(1, 0.01, 0.0001)
turn_pid =                  PIDController(1, 0.01, 0.0001)
jevois_handler =           JevoisHandler()
dead_tracker =              DeadReckoningTracker(gyro, left_motor, right_motor, 150 / 360 , motors_mounted_backwards=True)
point_navigator =           PointNavigator(dead_tracker, driver, turn_pid, straight_pid)
path_navigator =            PathNavigator(point_navigator, 1)
block_nav =                 BlockNavigator(driver, turn_pid)
picker_upper =              PickerUpper(joint_1_motor, joint_2_motor, gripper_motor, [150, 20])
path = ['''Pathing''']
checker = PersonChecker(jevois_handler)

while not path_navigator.path_completed:
    object_check = checker.operate()
    dead_tracker.update_position_and_heading()


    if object_check == True:
        if not block_nav.check_if_at_block():
            block_nav.step_toward_block(checker.goal_blob)
