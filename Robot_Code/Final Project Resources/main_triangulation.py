from PiStorms import PiStorms
from driver import Driver
from jevois_handler import JevoisHandler
from triangulation import TriangulationCalculator
from triangulation import TriangulationTracker

# Defining psm first because motors/sensors need it
psm = PiStorms()

# Defining motors and sensors
right_motor = psm.BAM1
left_motor = psm.BAM2
gyro_sensor = psm.BAS1
distance_sensor = psm.BBS2

# Initializing classes
driver = Driver(left_motor, right_motor, motors_mounted_backwards=True)
jevois_handler = JevoisHandler()
triangulation_calculator = TriangulationCalculator()
triangulation_tracker = TriangulationTracker(driver, gyro_sensor, jevois_handler, triangulation_calculator)

triangulation_tracker.begin_data_collection()
while not psm.isKeyPressed() and triangulation_tracker.is_data_collection_ongoing():
    triangulation_tracker.step()

driver.stop()
driver.step()
print "Robot location is: {}".format(triangulation_tracker.get_last_location())