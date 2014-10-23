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

class Launch():
    # Launch an existing APK
    def __init__(self, apk_name):
        self.apk_name = str(apk_name)

    def eval(self):
        return "adb_common.start_app(adb_path, '" + self.apk_name + "')\n"

class TypeText():
    # Convert a string into appropriate ADB commands
    def __init__(self, text_string, end_of_line):
        self.text_string = str(text_string)
        self.end_of_line = end_of_line

    def eval(self):
        text_to_return = "type_text_spaces(adb_path, ["

        text_arr = self.text_string.split(' ')

        for text in text_arr:
            text_to_return += "'" + text + "', "

        text_to_return = text_to_return[:-2] + "], "

        if self.end_of_line is True:
            text_to_return += "True)\n"
        else:
            text_to_return += "False)\n"

        return text_to_return

class Wait():
    # Introduces a wait into the script
    def __init__(self, wait_time) :
        self.wait_time = str(wait_time)

    def eval(self) :
        return "adb_common.android_wait(adb_path, " + self.wait_time + ")\n"

class PressScreen():
    # Create a screen press event
    def __init__(self, x_point, y_point) :
        self.x = str(x_point)
        self.y = str(y_point)

    def eval(self):
        return "adb_common.press(adb_path, " + self.x + ", " + self.y + ")\n"

class LongPressScreen():
    # Create a long screen press event
    def __init__(self, x_point, y_point):
        self.x = str(x_point)
        self.y = str(y_point)

    def eval(self):
        return "adb_common.long_press(adb_path, " + self.x + ", " + self.y + ")\n"

class Drag():
    # Create a drag event
    def __init__(self, x_start_point, y_start_point, x_end_point, y_end_point) :
        self.x_start = int(x_start_point)
        self.y_start = int(y_start_point)
        self.x_end = int(x_end_point)
        self.y_end = int(y_end_point)

    def eval(self):
        return "adb_common.swipe(adb_path, \"" + str(self.x_start) + "\", \"" + str(self.y_start) + "\", \"" + str(self.x_end) + "\", \"" + str(self.y_end) + "\")\n"

class Home():
    # Press the Home button
    def eval(self):
        return "adb_common.home(adb_path)\n"

class Menu():
    # Press the Menu button
    def eval(self):
        return "adb_common.menu(adb_path)\n"

class Back():
    # Press the Back button
    def eval(self):
        return "adb_common.back(adb_path)\n"

class Power():
    # Press the Power button
    def eval(self):
        return "adb_common.power(adb_path)\n"

#-------------------------------------------------------
 
class StmtList:
    # Builds and stores a list of Stmts
    def __init__(self):
        self.sl = []

    def insert(self, stmt):
        self.sl.insert(0, stmt)

    def eval(self):
        temp_string = "from subprocess import call\nimport adb_common\n\n"

        for s in self.sl:
            temp_string += s.eval()

        return temp_string
       
class Program:
    def __init__(self, stmt_list):
        self.stmt_list = stmt_list

    def eval(self):
        print self.stmt_list.eval()