import datetime

class PIDController(object):
    """PID class calculates appropriate response to smoothly reduce error over time."""

    def __init__(self, k_p, k_i, k_d):
        self.k_p = k_p
        self.k_i = k_i
        self.k_d = k_d

        self.previous_error = 0
        self.total_integral = 0
        self.previous_time = datetime.datetime.utcnow()

    def calculate_response(self, error):
        """Calculate an appropriate response to smoothly achieve a goal."""
        now = datetime.datetime.utcnow()
        length_of_step = now - self.previous_time
        length_of_step_milliseconds = length_of_step.microseconds / 1000

        self.total_integral += error * length_of_step_milliseconds
        error_change = error - self.previous_error

        P = error
        I = self.total_integral
        D = error_change / length_of_step_milliseconds

        result = self.k_p * P + self.k_i * I + self.k_d * D
        # print "PID returning result of: {0}. Step length {1}ms.".format(
        #     result, length_of_step_milliseconds)

        self.previous_error = error
        self.previous_time = now

        return result
