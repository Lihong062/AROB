'''Code Below processes the information from the Jevois Camera so that it is usable for code in the robot'''
import serial
import datetime
from serial.tools import list_ports

serdev = '/dev/ttyACM0'
# Look for an active serial port that includes "ACM".
for port in list_ports.grep('acm'):
    serdev = port.device

class JevoisFrame():
    # Creates a list of objects in the frame
    def __init__(self, id, objects):
        self.id = id
        self.objects = objects
        # All Jevois objects detected are given an ID

    def __repr__(self):
        if len(self.objects) > 0:
            return "Frame {} has {} objects: {}\n".format(
                self.id, len(self.objects), self.objects)
        else:
            return "Frame {} has no objects.\n".format(self.id)
        # Returns no object if necessary 

class JevoisObject():
    # Defines the jevois object 
    def __init__(self, object_id, x_coord, y_coord, width, height):
        self.object_id = object_id
        self.x_coord = int(x_coord)
        self.y_coord = int(y_coord)
        self.width = int(width)
        self.height = int(height)

    def __repr__(self):
        return "{} at ({},{}) size {}x{}".format(
            self.object_id, self.x_coord, self.y_coord,
            self.width, self.height)
 
# Code referenced from Jevois website support. 
class JevoisHandler():
    # Handler has the fuction to get the object in the frame
    def getObjects(self):
        return self.getFrame().objects

    def getFrame(self):
        frame = None
        start_time = datetime.datetime.utcnow()
        with serial.Serial(serdev, 115200, timeout=0.1) as ser:
            while self.milliseconds_passed(start_time) < 100:
                # Read a whole line & strip any trailing line ending character:
                line = ser.readline().rstrip()

                # Split the line into tokens:
                tok = line.split()

                # Skip if timeout or malformed line:
                if (len(tok) == 7) and (tok[1] == 'N2'):
                    # Assign some named Python variables to the tokens:
                    frame_id, message_type, object_id, x, y, w, h = tok


                    obj = JevoisObject(object_id, x, y, w, h)
                    if frame == None:
                        frame = JevoisFrame(frame_id, [obj])
                    if (frame.id == frame_id):
                        if not (obj in frame.objects):
                            frame.objects.append(obj)
                    else:
                       return frame
        return JevoisFrame(0, [])

    def milliseconds_passed(self, start_time):
        now = datetime.datetime.utcnow()
        diff = now - start_time
        return diff.microseconds / 1000