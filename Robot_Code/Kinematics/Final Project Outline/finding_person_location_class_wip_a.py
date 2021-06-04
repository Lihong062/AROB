from person_data_class_wip_a import PersonData
import math
class FindingPersonLocation(object):
    def __init__(self, driver, tracker, turn_pid, block_navigator, triangulation_tracker, handler, checker):
        self.driver = driver
        self.block_navigator = block_navigator
        self.triangulation_tracker = triangulation_tracker
        self.people_record_list = []
        self.tracker = tracker
        self.handler = handler
        self.goal_blob = None
        self.turn_pid = turn_pid
        self.checker = checker
    def step(self):
        self.goal_blob = self.checker.get_goal_blob()


        self.turn_to_closest_person(self.goal_blob)
        self.past_people_check(self.people_record_list, self.tracker.get_location)



    def turn_to_closest_person(self, goal_blob):
        turn_speed = 10
        # turn_speed = self.turn_pid.calculate_response(goal_blob.x_coord)

        if goal_blob.x_coord > -25 and goal_blob.x_coord < 25:
            print "pointed at person"
            return

        if goal_blob.x_coord > 0:
            print "right turn"
            self.driver.turn_right(turn_speed)
        else:
            print "left turn"
            self.driver.turn_left(turn_speed)



    def past_people_check(self, people_list, heading):
        ##return boolean
        ##check block list, do math with heading,
        ##return true if we've seen the block before, false if not
        heading = heading
        robot_spot = self.tracker.get_location()

        if people_list == []:
            print "new person"
            return False
        for person in people_list:
            correct_heading = self._people_check_math(person, robot_spot)
            heading_error = ((correct_heading - heading + 180) % 360) - 180

            if heading_error > -3 and heading_error < 3:
                return True
        return False

    def _people_check_math(self, person, robot_spot):
            x1 = person.x * 1.0
            y1 = person.y * 1.0

            x2 = robot_spot[0] * 1.0
            y2 = robot_spot[1] * 1.0

            distance = ((x1 - x2)**2 + (y1 - y2)**2)**.5

            delta_x = x2-x1
            delta_y = y2-y1

            proper_heading = math.degrees(math.atan2(delta_y, delta_x))
            return proper_heading
