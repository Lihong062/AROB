
class BlockNavigator(object):
    """Navigates to a specific block and stops when it arrives."""
    def __init__(self, driver, turn_pid):
        self.driver = driver
        self.turn_pid = turn_pid
        self.currently_at_block = False

    def step_toward_block(self, block):
        """Take one step towards a block."""

        center_threshold = 100  # Feel free to tune this
        width_threshold = 800   # Feel free to tune this

        if block.width > width_threshold:
            # print "block is close - stopping"
            self.currently_at_block = True
            self.driver.stop()
        elif block.x_coord > -center_threshold and block.x_coord < center_threshold:
            # print "block is centered - moving forward"
            self.currently_at_block = False
            self.driver.go_straight(20)
        elif block.x_coord <= -center_threshold:
            self.currently_at_block = False
            turning_speed = self.turn_pid.calculate_response(abs(block.x_coord))
            # print "block is at {}, turning left at speed {}".format(block.x_coord, turning_speed)
            self.driver.turn_left(turning_speed)
        elif block.x_coord >= center_threshold:
            self.currently_at_block = False
            turning_speed = self.turn_pid.calculate_response(abs(block.x_coord))
            # print "block is at {}, turning right at speed {}".format(block.x_coord, turning_speed)
            self.driver.turn_right(turning_speed)
        self.driver.step()

    def check_if_at_block(self):
        """Return True if at the block, else False."""
        return self.currently_at_block
