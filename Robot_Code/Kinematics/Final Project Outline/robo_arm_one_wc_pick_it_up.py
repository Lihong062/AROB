
from PiStorms                           import PiStorms
import numpy as np
import matplotlib.pyplot as plt
from kinematics_class_wc_pick_it_up             import Joint
from kinematics_class_wc_pick_it_up             import JointMotor
from kinematics_class_wc_pick_it_up             import ForwardKinematics
from inverse_kinematics_class_wc_pick_it_up     import InverseKinematics
from gripper_class                              import Gripper
import math
import time


class picker_upper(object):
    def __init__(self, joint_motor_1, joint_motor_2, gripper_motor, goal_point):
        self.joint_motor_1 =             joint_motor_1
        self.joint_motor_2 =             joint_motor_2
        self.gripper_motor =             gripper_motor

        self.kinemation =                ForwardKinematics()
        self.inverse_kinemation =        InverseKinematics(self.kinemation)

        self.goal_point =                goal_point

        self.joint_1 =                   Joint(165, 0, 0, [-25, 19])
        self.joint_2 =                   Joint(117, 0, 0, [-150, 21])
        self.joint_origin =              Joint(0, 97, 0, [])
        self.joints =                    [self.joint_origin, self.joint_1, self.joint_2]
        self.object_joint_motor_1 =      JointMotor(self.joint_motor_1, 5.0)
        self.object_joint_motor_2 =      JointMotor(self.joint_motor_2, 2.0)
        self.gripper =                   Gripper(self.gripper_motor)

    def grab_it(self, angles):
        angles = self.inverse_kinemation.calculateJointAngles(self.goal_point, self.joints)

        self.joint_1.angle =             angles[0]
        self.joint_2.angle =             angles[1]

        self.object_joint_motor_2.set_goal_position(self.joint_2.angle)
        self.object_joint_motor_1.set_goal_position(self.joint_1.angle)

        while not (self.object_joint_motor_1.at_pos and self.object_joint_motor_2.at_pos):
            if self.object_joint_motor_1.at_pos == False:
                self.object_joint_motor_1.step()
            if self.object_joint_motor_2.at_pos == False:
                self.object_joint_motor_2.step()

        time.sleep(2)
        self.gripper.grip()
        time.sleep(2)

        self.object_joint_motor_2.set_goal_position(-1 * self.joint_2.angle)
        self.object_joint_motor_1.set_goal_position(-1 * self.joint_1.angle)

        while not (self.object_joint_motor_1.at_pos and self.object_joint_motor_2.at_pos):
            if self.object_joint_motor_1.at_pos == False:
                self.object_joint_motor_1.step()
            if self.object_joint_motor_2.at_pos == False:
                self.object_joint_motor_2.step()

        self.object_joint_motor_2.set_goal_position(90)
        self.object_joint_motor_1.set_goal_position(70)

        while not (self.object_joint_motor_1.at_pos and self.object_joint_motor_2.at_pos):
            if self.object_joint_motor_1.at_pos == False:
                self.object_joint_motor_1.step()
            if self.object_joint_motor_2.at_pos == False:
                self.object_joint_motor_2.step()

        self.gripper.release()

        self.object_joint_motor_2.set_goal_position(-90)
        self.object_joint_motor_1.set_goal_position(-70)

        while not (self.object_joint_motor_1.at_pos and self.object_joint_motor_2.at_pos):
            if self.object_joint_motor_1.at_pos == False:
                self.object_joint_motor_1.step()
            if self.object_joint_motor_2.at_pos == False:
                self.object_joint_motor_2.step()
