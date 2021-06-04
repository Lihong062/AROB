from jevois_handler import JevoisHandler


jev = JevoisHandler()

def testGetFrame():
    for i in range(20):
        frame = jev.getFrame()
        print frame
        i += 1

def testGetObjects():
    for i in range(20):
        objects = jev.getObjects()
        print objects
        i += 1


print "testing getFrame function:"
testGetFrame()

print "\n\ntesting getObjects function:"
testGetObjects()