import math

class DeadReckoningTracker(object):
    # DeadReckoningTracker class tracks robot position and heading using gyro and motor sensors

    def __init__(self, gyro_sensor, left_motor, right_motor, mms_moved_per_motor_degree, motors_mounted_backwards=False):
        self.gyro_sensor = gyro_sensor
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.mms_moved_per_motor_degree = mms_moved_per_motor_degree
        self.motors_mounted_backwards = motors_mounted_backwards

        self.current_x = 0
        self.current_y = 0
        self.heading = 0
        self.initial_gyro_degrees = gyro_sensor.gyroAngleEV3()

        self.previous_left_motor_pos = left_motor.pos()
        self.previous_right_motor_pos = right_motor.pos()

    def update_position_and_heading(self):
        # Update the position and heading of the robot.
        # Safely gather data from the sensors, exiting if an error occurs (Using try-except structure).
        try:
            gyro_degrees = self.gyro_sensor.gyroAngleEV3()
            left_motor_pos = self.left_motor.pos()
            right_motor_pos = self.right_motor.pos()
        except Exception as ex:
            print ex
            return

        # Get the angle from the sensor, calibrated against start point
        self.heading = ((gyro_degrees - self.initial_gyro_degrees) * -1) % 360

        # Gather the position from both motor encoders
        left_motor_degrees_changed = left_motor_pos - self.previous_left_motor_pos
        right_motor_degrees_changed = right_motor_pos - self.previous_right_motor_pos

        # Save motor positions for next time
        self.previous_right_motor_pos = right_motor_pos
        self.previous_left_motor_pos = left_motor_pos

        if abs(left_motor_degrees_changed) > 10000 or abs(right_motor_degrees_changed) > 10000:
            # Does not record data if out of an absurdly large range 
            print "DeadReckoningTracker encountered error reading motor encoders."
            return

        # Calculate the distance travelled by averaging both motors and converting degs to mms.
        average_degrees_moved = (left_motor_degrees_changed + right_motor_degrees_changed) / 2
        distance_traveled_mms = average_degrees_moved * self.mms_moved_per_motor_degree

        if self.motors_mounted_backwards:
            distance_traveled_mms = distance_traveled_mms * -1

        # Use trig to calculate X and Y travelled using heading and distance travelled.
        x_traveled = math.cos(math.radians(self.heading)) * distance_traveled_mms
        y_traveled = math.sin(math.radians(self.heading)) * distance_traveled_mms

        # Update current position using the most recent x and y changes.
        self.current_x += x_traveled
        self.current_y += y_traveled

    def get_location(self):
        """Return the current location of the robot."""
        return [self.current_x, self.current_y]

    def get_heading(self):
        """Return the current heading of the robot."""
        return self.heading
