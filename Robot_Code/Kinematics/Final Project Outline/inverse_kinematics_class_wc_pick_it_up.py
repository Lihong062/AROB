from kinematics_class_wc_pick_it_up import Joint

class InverseKinematics(object):
    def __init__(self, forward_kinematics):
        self.forward_kinematics = forward_kinematics
        self.positions = []
        self.angle_combos = []
    def calculateJointAngles(self, desired_gripper_position, joints):

        for angle1 in range(joints[1].angle_range[0], joints[1].angle_range[1]):
            for angle2 in range(joints[2].angle_range[0], joints[2].angle_range[1]):

                # print 'Using angles ', angle1, angle2
                joint0 = joints[0]
                joint1 = Joint(165, 0, angle1, [])
                joint2 = Joint(117, 0, angle2, [])
                joint_list = [joint0, joint1, joint2]
                angle_list = [angle1, angle2]


                if self._are_joint_angles_valid([angle1, angle2]):
                    pos = self.forward_kinematics.calculateGripperPosition(joint_list)
                    self.positions.append(pos)
                    self.angle_combos.append(angle_list)
                    if self.distance_formula(pos, desired_gripper_position) < 5:
                        print 'successful calculation'
                        print angle_list
                        return angle_list

        print 'failed to calculate'

        """
        Args:
           desired_gripper_position: A 2x1 location vector
           joints: A list of joint objects describing the robot (angles will be ignored)
        Returns:
           A list of the joint angles to implement, or False if impossible."""

    def _are_joint_angles_valid(self, joint_angles):
        #####
        #####STRETCH GOAL: implement function such using forward kinematics and joint 2 location to test if in floor
        #####c_2_kinda

        return True

    def distance_formula(self, position_1, position_2):
        x1 = position_1[0][0]
        y1 = position_1[1][0]
        x2 = position_2[0]
        y2 = position_2[1]

        distance = ((x1 - x2)**2 + (y1 - y2)**2)**.5
        # print 'distance is', distance
        return distance