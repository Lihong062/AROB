from matplotlib import pyplot

FILE_NAME = "/home/pi/Pictures/robot_position.png"

class Mapper(object):
    """Mapper class keeps track locations discovered and travelled by the robot."""
    def __init__(self, psm):
        self.psm = psm

        self.robot_path = []
        pyplot.figure(figsize=(4, 3), dpi=80)
        pyplot.title('Robot position')
        pyplot.xlabel('x')
        pyplot.ylabel('y')
        pyplot.grid(True)

    def add_robot_location(self, location):
        """Add an new position to the robot's path."""
        self.robot_path.append(location)

    def plot(self):
        """Create, save, and display a plot of the robot's location."""
        pyplot.plot([location[0] for location in self.robot_path],
                    [location[1] for location in self.robot_path])
        pyplot.tight_layout() # make sure the entire plot fits on screen
        pyplot.savefig(FILE_NAME, format="png") # save it
        self.psm.screen.fillBmp(0, 0, 320, 240, FILE_NAME) # show it on PiStorms screen
