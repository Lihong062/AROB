from PiStorms               import PiStorms
import numpy as np
import math
from kinematics_class_wip_a import Joint
from kinematics_class_wip_a import JointMotor
from kinematics_class_wip_a import ForwardKinematics
psm =                       PiStorms()

joint_motor_1 =             psm.BBM1
joint_motor_2 =             psm.BAM2
gripper_motor =             psm.BAM1
wheel_motor =               psm.BBM2

joint_1_angle =             30
joint_2_angle =             -30

joint_1 =                   Joint(135, 0, joint_1_angle)
joint_2 =                   Joint(125, 0, joint_2_angle)
joint_origin =              Joint(0, 55, 0)
joints =                    [joint_origin, joint_1, joint_2]
object_joint_motor_1 =      JointMotor(joint_motor_1)
object_joint_motor_2 =      JointMotor(joint_motor_2)

kinemation =                ForwardKinematics()

# def main():
#     while not psm.isKeyPressed():
#

print kinemation.calculateGripperPosition(joints)
