import sys

adbEvents = open(sys.argv[1], "r")
array = []

for line in adbEvents:
        array.append(line)

deviceX = 53
deviceY = 54
startStopPrefix = 3
startStop = 57
counter = 0
emulator = False

if len(sys.argv) == 3 and sys.argv[2] == "emulator":
    deviceX = 0
    deviceY = 1
    startStopPrefix = 1
    startStop = 330
    emulator = True

adbEvents.close()
 
startX = 0
startY = 0
lastX = 0
lastY = 0
touchStart = False
touchEnd = False

for element in array:
    if str(element[:18]) == "/dev/input/event0:":
        parts = element.split()

        if (int(parts[1], 16) == 3) and (int(parts[2], 16) == deviceX):
            lastX = int(parts[3], 16)
            counter += 1
            if startX == 0:
                startX = lastX
        elif (int(parts[1], 16) == 3) and (int(parts[2], 16) == deviceY):
            lastY = int(parts[3], 16)
            counter += 1
            if startY == 0:
                startY = lastY
        elif (int(parts[1], 16) == startStopPrefix) and (int(parts[2], 16) == startStop) and touchStart is False:
            touchStart = True
        elif (int(parts[1], 16) == startStopPrefix) and (int(parts[2], 16) == startStop) and touchStart is True:
            touchEnd = True

            if touchStart and touchEnd:
                touchStart = False
                touchEnd = False

                # Print result
                if emulator:
                    if startX == lastX and startY == lastY:
                        print "PRESS " + str(lastX) + " " + str(lastY) + ";"
                    elif startX != lastX or startY != lastY:
                        print "DRAG " + str(startX) + " " + str(startY) + " " + str(lastX) + " " + str(lastY) + ";"
                else:
                    if counter <= 10:
                        print "PRESS " + str(lastX) + " " + str(lastY) + ";"
                    elif startX != lastX or startY != lastY:
                        print "DRAG " + str(startX) + " " + str(startY) + " " + str(lastX) + " " + str(lastY) + ";"

                startX = 0
                startY = 0
                lastX = 0
                lastY = 0
