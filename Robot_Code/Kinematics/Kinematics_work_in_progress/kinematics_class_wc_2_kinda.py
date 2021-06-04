import numpy as np
import math


class Joint(object): # Simple class to clearly store joint information
    def __init__(self, x_length_in_mm, y_length_in_mm, angle_in_degrees, angle_range):
        self.x_length = x_length_in_mm
        self.y_length = y_length_in_mm
        self.angle = angle_in_degrees

        self.angle_range = angle_range

class JointMotor(object):
    """A wrapper for motor that can keep it at a certain position."""
    def __init__(self, motor, gear_ratio_second_to_first):
        self.motor = motor
        self.gear_ratio = gear_ratio_second_to_first

    def set_goal_position(self, position):
        """Set the goal position of the motor."""
        self.goal_pos = -1 * position

    def step(self):
        """Take a step towards having the motor in the right position."""
        pos = self.motor.pos() / self.gear_ratio
        print pos
        if abs(pos - self.goal_pos) <= 5:
            print "braking"
            self.motor.brake()
            # self.motor.hold()
        elif pos > self.goal_pos + 5:
            print "Turning positive"
            self.motor.setSpeed(-5)
        elif pos < self.goal_pos - 5:
            print "Turning negetive"
            self.motor.setSpeed(5)

class ForwardKinematics(object):
    def calculateGripperPosition(self, joints):
        """Do the calculations, and return P0 (gripper position in standard coordinate plane)"""
        position_K = np.array([[joints[-1].x_length], [joints[-1].y_length]])     ###Define pos k for first iteration of loop

        for i in range(1, len(joints)):
            joint_k = joints[len(joints) - i]                      ###sets joints k and k-1 for use in algorithm
            joint_k_minus_1 = joints[len(joints) - i - 1]          ###

            x_K_minus_1 = joint_k_minus_1.x_length                 ###Establishes inputs to reference shift
            y_K_minus_1 = joint_k_minus_1.y_length
            theta_K = joint_k.angle

            position_K = self._shift_reference_frame_K_to_K_minus_1(position_K, theta_K, x_K_minus_1, y_K_minus_1)


        print 'gripper position of this set is', position_K
        return position_K

    def _shift_reference_frame_K_to_K_minus_1(self, position_K, theta_K, x_K_minus_1, y_K_minus_1):
        """Shift reference frame from K+1 to K by calculating the rotation and translation matrices required."""
        m_rot = np.array([[cos(theta_K), -1 * sin(theta_K)],     ###Rotation Matrix
                          [sin(theta_K), cos(theta_K)]])
        # print "rot is:", m_rot.shape

        m_pos = np.array([position_K[0],                       ###Position Matrix (that will be rotated)
                          position_K[1]])
        # print "pos is: ", m_pos.shape

        m_xy = np.array([[x_K_minus_1],                          ###Translation matrix
                         [y_K_minus_1]])
        # print "xy is:", m_xy.shape

        pos_k_minus_1 = np.matmul(m_rot, m_pos) + m_xy          ###Transformation calculation
        # print "k is:", pos_k_minus_1.shape
        # print "Iteration completed"
        return pos_k_minus_1


###HELPER
def cos(degrees):
    return math.cos(math.radians(degrees))

def sin(degrees):
    return math.sin(math.radians(degrees))









# Example code as to how this could be used
# joint0 = Joint(0, 0, "Meaningless angle!") # Translation from origin to first joint
# joint1 = Joint(x1, y1, theta_1) # The angle of your first motor and your first arm length
# # Other joints as necessary
# joints = [joint0, joint1, ...] # add a 2nd joint, and a third if necessary

# kinematicsCalculator = ForwardKinematics()
# p0 = kinematicsCalculator.calculateGripperPosition(joints)

# print "Gripper is at: {}".format(p0)

# ## Demo code showing Numpy matrix multiplication
# import numpy as np

# a = [[1, 2], [3, 4]]
# b = [5, 6]

# print np.matmul(a, b) ## Returns [17, 39]