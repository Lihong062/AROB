class Joint(object): # Simple class to clearly store joint information
    def __init__(self, x_length_in_mm, y_length_in_mm, angle_in_degrees):
        self.x_length = x_length_in_mm
        self.y_length = y_length_in_mm
        self.angle = angle_in_degrees

class JointMotor(object):
    """A wrapper for motor that can keep it at a certain position."""
    def __init__(self, motor):
        pass

    def set_goal_position(self, position):
        """Set the goal position of the motor."""
        return

    def step(self):
        """Take a step towards having the motor in the right position."""
        return

class ForwardKinematics(object):
    def calculateGripperPosition(self, joints):
        """Do the calculations, and return P0 (gripper position in standard coordinate plane)"""
        return

    def _shift_reference_frame_K_to_K_minus_1(self, position_K, theta_K, x_K_minus_1, y_K_minus_1):
        """Shift reference frame from K+1 to K by calculating the rotation and translation matrices required."""
        return

class InverseKinematics(object):
    def __init__(self, forward_kinematics):
        pass

    def calculateJointAngles(self, desired_gripper_position, joints):
        """Produce a list of joint angles to produce a desired gripper location.

        Args:
           desired_gripper_position: A 2x1 location vector
           joints: A list of joint objects describing the robot (angles will be ignored)
        Returns:
           A list of the joint angles to implement, or False if impossible."""
        return

    def _are_joint_angles_valid(self, joint_angles):
        """Return True if this set of angles is safe for your arm, else False"""
        return


# Example code as to how this could be used
joint0 = Joint(0, 0, "Meaningless angle!") # Translation from origin to first joint
joint1 = Joint(x1, y1, theta_1) # The angle of your first motor and your first arm length
# Other joints as necessary
joints = [joint0, joint1, ...] # add a 2nd joint, and a third if necessary

kinematicsCalculator = ForwardKinematics()
p0 = kinematicsCalculator.calculateGripperPosition(joints)

print "Gripper is at: {}".format(p0)

## Demo code showing Numpy matrix multiplication
import numpy as np

a = [[1, 2], [3, 4]]
b = [5, 6]

print np.matmul(a, b) ## Returns [17, 39]