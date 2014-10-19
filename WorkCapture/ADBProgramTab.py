# Android Debug Bridge Script Generator
# Takes seven different statements and transforms them into a useable script for automating Android tasks
#       Grammar:
#               program: stmt_list
#               stmt_list:  stmt ';' stmt_list
#                   |   stmt ';'
#                               stmt : launch_stmt
#                                       | typetext_stmt
#                                       | press_stmt
#                                       | longpress_stmt
#                                       | home_stmt
#                                       | menu_stmt
#                                       | back_stmt
#                                       | drag_stmt
#                               launch_stmt : LAUNCH TEXT
#                               typetext_stmt : TYPETEXT TEXT
#                               press_stmt : PRESS NUMBER NUMBER
#                               longpress_stmt : LONGPRESS NUMBER NUMBER
#                               drag_stmt: DRAG TEXT TEXT TEXT TEXT
#                               home_stmt : HOME
#                               menu_stmt : MENU
 
import sys
 
class Launch() :
        '''Launch an existing APK'''
        def __init__(self, APKName) :
                self.apkName = str(APKName)
       
        def eval(self) :
                return "./adb shell am start -n " + self.apkName + "\n"
 
class TypeText() :
        '''Convert a string into appropriate ADB commands'''
        def __init__(self, TextString, EndOfLine) :
                self.textString = str(TextString)
                self.endOfLine = EndOfLine
       
        def eval(self) :
                self.textString = self.textString.replace(" ", "\n./adb shell input keyevent 62\n./adb shell input text ")

                textToReturn = "./adb shell input text " + self.textString + "\n"
                if self.endOfLine == True : textToReturn += "./adb shell input keyevent 66\n" 
                
                return textToReturn 

class Wait() :
        '''Introduces a wait into the script'''
        def __init__(self, WaitTime) :
                self.waitTime = str(WaitTime)
       
        def eval(self) :
                return "./adb shell sleep " + self.waitTime + "\n"

class PressScreen() :
        '''Create a screen press event'''
        def __init__(self, xPoint, yPoint) :
                self.x = str(xPoint)
                self.y = str(yPoint)
 
        def eval(self) :
		screenString = "./adb shell sendevent /dev/input/event0 3 57 1800\n"
		screenString += "./adb shell sendevent /dev/input/event0 3 53 " + self.x + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 3 54 " + self.y + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 0 0 0\n"
                screenString += "./adb shell sendevent /dev/input/event0 3 57 4294967295\n"
                screenString += "./adb shell sendevent /dev/input/event0 0 0 0\n"
 
                return screenString
 
class LongPressScreen() :
        '''Create a long screen press event'''
        def __init__(self, xPoint, yPoint) :
                self.x = str(xPoint)
                self.y = str(yPoint)
 
        def eval(self) :
		screenString = "./adb shell sendevent /dev/input/event0 3 57 1800"
		screenString += "./adb shell sendevent /dev/input/event0 3 53 " + self.x + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 3 54 " + self.y + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 0 0 0\n"
                screenString += "./adb shell sleep 3\n"
                screenString += "./adb shell sendevent /dev/input/event0 3 57 4294967295\n"
                screenString += "./adb shell sendevent /dev/input/event0 0 0 0\n"
 
                return screenString

class Drag() :
        '''Create a drag event'''
        def __init__(self, xStartPoint, yStartPoint, xEndPoint, yEndPoint) :
                self.xStart = int(xStartPoint)
                self.yStart = int(yStartPoint)
                self.xEnd = int(xEndPoint)
                self.yEnd = int(yEndPoint)
 
        def eval(self) :
                # Figure out if the distance is 0
                xDistance = self.xEnd - self.xStart
                yDistance = self.yEnd - self.yStart

                # Touch the starting point
		screenString = "./adb shell sendevent /dev/input/event0 3 57 1800\n"
                screenString += "./adb shell sendevent /dev/input/event0 3 53 " + str(self.xStart) + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 3 54 " + str(self.yStart) + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 0 0 0\n"

		# Touch the ending point
                screenString += "./adb shell sendevent /dev/input/event0 3 53 " + str(self.xEnd) + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 3 54 " + str(self.yEnd) + "\n"
                screenString += "./adb shell sendevent /dev/input/event0 0 0 0\n"

		# End the sequence
                screenString += "./adb shell sendevent /dev/input/event0 3 57 4294967295\n"
                screenString += "./adb shell sendevent /dev/input/event0 0 0 0\n"
 
                return screenString
 
class Home() :
        '''Press the Home button'''
        def eval(self) :
                return "./adb shell input keyevent 3\n"
 
class Menu() :
        '''Press the Menu button'''
        def eval(self) :
                return "./adb shell input keyevent 1\n"
 
class Back() :
        '''Press the Back button'''
        def eval(self) :
                return "./adb shell input keyevent 4\n"
 
#-------------------------------------------------------
 
class StmtList :
        '''builds/stores a list of Stmts'''
       
        def __init__(self) :
                self.sl = []
       
        def insert(self, stmt) :
                self.sl.insert( 0, stmt )
       
        def eval(self) :
                tempString = "cd /lib/android/sdk/platform-tools\n"
                for s in self.sl :
                        tempString += s.eval()
 
                return tempString
       
class Program :
        def __init__(self, stmtList) :
                self.stmtList = stmtList
       
        def eval(self) :
                print self.stmtList.eval()
