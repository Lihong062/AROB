from enum import Enum

class Direction(Enum):
    # Enum for setting goal direction.
    STOP = 0
    STRAIGHT = 1
    RIGHT = 2
    LEFT = 3
    BACKWARDS = 4

class Driver(object):
    # Driver class can move a robot with a certain direction goal and speed goal.

    def __init__(self, left_motor, right_motor, motors_mounted_backwards=False):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.motors_mounted_backwards = motors_mounted_backwards

        self.motor_speed = 0
        self.direction = Direction.STOP

    # Functions to change the goal
    def stop(self):
        self.direction = Direction.STOP
        self.motor_speed = 0

    def go_straight(self, speed):
        self.direction = Direction.STRAIGHT
        self.motor_speed = self._safety_cap_speed(speed)

    def turn_right(self, speed):
        self.direction = Direction.RIGHT
        self.motor_speed = self._safety_cap_speed(speed)

    def turn_left(self, speed):
        self.direction = Direction.LEFT
        self.motor_speed = self._safety_cap_speed(speed)

    def go_backwards(self, speed):
        self.direction = Direction.BACKWARDS
        self.motor_speed = self._safety_cap_speed(-speed)
    # End of goal-changing functions

    def step(self):
        # Advance the goal one step.
        # print "Driving direction: {0} at speed: {1}".format(self.direction, self.motor_speed)
        if self.direction == Direction.STOP:
            self.left_motor.brake()
            self.right_motor.brake()
        elif self.direction == Direction.STRAIGHT:
            self.left_motor.setSpeed(self.motor_speed)
            self.right_motor.setSpeed(self.motor_speed)
        elif self.direction == Direction.RIGHT:
            self.left_motor.setSpeed(self.motor_speed)
            self.right_motor.setSpeed(-1 * self.motor_speed)
        elif self.direction == Direction.LEFT:
            self.left_motor.setSpeed(-1 * self.motor_speed)
            self.right_motor.setSpeed(self.motor_speed)
        elif self.direction == Direction.BACKWARDS:
            self.left_motor.setSpeed(-1 * self.motor_speed)
            self.right_motor.setSpeed(-1 * self.motor_speed)

    # Safety cap to prevent values over 100
    def _safety_cap_speed(self, speed):
        if self.motors_mounted_backwards:
            speed = speed * -1
        if speed > 100:
            return 100
        if speed < -100:
            return -100
        return speed
