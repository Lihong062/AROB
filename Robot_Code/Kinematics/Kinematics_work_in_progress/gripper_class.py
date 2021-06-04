import time
class Gripper(object):
    def __init__(self, motor):
        self.motor = motor

    def grip(self):
        print "gripping"
        self.motor.setSpeed(5)
        time.sleep(2)
        self.motor.resetPos()
        self.motor.hold
    def release(self):
        print "releasing"
        self.motor.setSpeed(-5)
        time.sleep(2)
        self.motor.resetPos()
        self.motor.hold