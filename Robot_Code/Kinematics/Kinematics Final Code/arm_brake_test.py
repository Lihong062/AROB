from PiStorms import PiStorms

psm = PiStorms()


while True:
    # psm.BAM1.hold()
    # psm.BAM2.hold()
    # psm.BBM1.hold()
    # psm.BBM2.hold()
    print 'joint 1 pos', psm.BBM1.pos()
    print 'joint 2 pos', psm.BAM2.pos()
    # print 'gripper pos', psm.BAM1.pos()
    ##Wheels is BBM2
    ##Claw is BAM1

    # psm.BAM1.brake()
    # psm.BAM2.brake()
    # psm.BBM1.brake()
    # psm.BBM2.brake()