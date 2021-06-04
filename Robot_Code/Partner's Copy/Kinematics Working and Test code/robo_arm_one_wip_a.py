from PiStorms                           import PiStorms
import numpy as np
import math
import time
import matplotlib.pyplot as plt
from kinematics_class_wip_a             import Joint
from kinematics_class_wip_a             import JointMotor
from kinematics_class_wip_a             import ForwardKinematics
from inverse_kinematics_class_wip_a     import InverseKinematics
from gripper_class                      import Gripper

psm =                       PiStorms()

joint_motor_1 =             psm.BBM1
joint_motor_2 =             psm.BAM2
gripper_motor =             psm.BAM1
wheel_motor =               psm.BBM2

kinemation =                ForwardKinematics()
inverse_kinemation =        InverseKinematics(kinemation)

goal_point =                [200, 20]

joint_1 =                   Joint(165, 0, 0, [-25, 19])
joint_2 =                   Joint(117, 0, 0, [-150, 21])
joint_origin =              Joint(0, 97, 0, [])
joints =                    [joint_origin, joint_1, joint_2]
object_joint_motor_1 =      JointMotor(joint_motor_1, 5.0)
object_joint_motor_2 =      JointMotor(joint_motor_2, 2.0)
gripper =                   Gripper(gripper_motor)


angles = inverse_kinemation.calculateJointAngles(goal_point, joints)

joint_1.angle =             angles[0]
joint_2.angle =             angles[1]

# x_list = [item[0][0] for item in inverse_kinemation.positions]
# y_list = [item[1][0] for item in inverse_kinemation.positions]

# plt.plot(x_list, y_list, 'ro')
# plt.show()

object_joint_motor_2.set_goal_position(joint_2.angle)
object_joint_motor_1.set_goal_position(joint_1.angle)

while not (object_joint_motor_1.at_pos and object_joint_motor_2.at_pos):
    if object_joint_motor_1.at_pos == False:
        object_joint_motor_1.step()
    if object_joint_motor_2.at_pos == False:
        object_joint_motor_2.step()

gripper.grip()
time.sleep(2)

object_joint_motor_2.set_goal_position(-1 * joint_2.angle)
object_joint_motor_1.set_goal_position(-1 * joint_1.angle)


while not (object_joint_motor_1.at_pos and object_joint_motor_2.at_pos):
    if object_joint_motor_1.at_pos == False:
        object_joint_motor_1.step()
    if object_joint_motor_2.at_pos == False:
        object_joint_motor_2.step()

gripper.release()


# print kinemation.calculateGripperPosition(joints)
