from PiStorms import PiStorms
from driver import Driver
from jevois_handler import JevoisHandler
from block_navigator import BlockNavigator
from triangulation import TriangulationCalculator
from triangulation import TriangulationTracker

# Defining psm first because motors/sensors need it
psm = PiStorms()

# Defining motors and sensors
right_motor = psm.BAM1
left_motor = psm.BBM1
gyro_sensor = psm.BBS1
distance_sensor = psm.BAS1

# Initializing classes
driver = Driver(left_motor, right_motor)
jevois_handler = JevoisHandler()
navigator = BlockNavigator(driver)
triangulation_calculator = TriangulationCalculator()
triangulation_tracker = TriangulationTracker(driver, gyro_sensor, jevois_handler, triangulation_calculator)

while not psm.isKeyPressed():
    objects = jevois_handler.getObjects()
    blobs = [obj for obj in objects if obj.object_id == "blob0"]  # Build a list of blob0 objects
    if not blobs:
        continue  # No blobs detected, so start the loop again.

    blobs.sort(key=lambda obj: obj.width, reverse=True)  # Sort the list of blobs by width, largest first
    blob_to_target = blobs[0]  # Get the largest blob
    if navigator.checkIfAtBlock(blob_to_target):
        break  # Exit the loop, since we've reached the block
    navigator.stepTowardBlock(blob_to_target)  # Since we see a block but haven't reached it, move towards it.

print "Block reached.  Gathering data about location."
triangulation_tracker.begin_data_collection()
while not psm.isKeyPressed() and triangulation_tracker.is_data_collection_ongoing():
    triangulation_tracker.step()

driver.stop()
driver.step()
print "Robot location is: {}".format(triangulation_tracker.get_last_location())
