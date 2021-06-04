class PathNavigator(object):
    """PathNavigator moves the robot through a series of points."""
    def __init__(self, point_navigator, acceptable_error_mms):
        self.point_navigator = point_navigator
        self.acceptable_error_mms = acceptable_error_mms

        self.path = []
        self.current_goal_path_index = 0
        self.path_completed = False

    def append_new_point_to_path(self, point):
        """Add a point to the path."""
        self.path.append(point)
        self.path_completed = False

    def set_path(self, path):
        """Overwrite the entire path."""
        self.path = path
        self.current_goal_path_index = 0
        self.point_navigator.set_point_goal(self.path[self.current_goal_path_index])
        self.path_completed = False

    def step(self):
        """Take a step towards the next point in the path."""
        if self.point_navigator.get_distance_to_goal() < self.acceptable_error_mms:
            self.change_goal_to_next_point()
        self.point_navigator.step()

    def change_goal_to_next_point(self):
        """If there are more goals in the list, update to the next available goal."""
        if self.current_goal_path_index < (len(self.path)-1):
            self.current_goal_path_index += 1
            new_goal = self.path[self.current_goal_path_index]
            print "Path Navigator: Setting next goal as {}".format(new_goal)
            self.point_navigator.set_point_goal(new_goal)
        else:
            print "Path Navigator: I have finished the path!"
            self.path_completed = True

    def is_path_completed(self):
        """Returns true if the robot has reached all points in the path."""
        return self.path_completed
