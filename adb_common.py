from subprocess import call
import vars


def power():
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "1", "116", "1"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "0", "0", "0"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "1", "116", "0"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "0", "0", "0"])


def apk_inst(apk_name):
	call([vars.adb_path + "adb", "install", apk_name])


def apk_inst_chk(apk_var_name):
    if vars.apks[apk_var_name]['installed'] is False:
        apk_inst(vars.apks[apk_var_name]['path'])
        vars.apks[apk_var_name]['installed'] = True


def apk_uninst(apk_var_name):
    if vars.apks[apk_var_name]['installed'] is True:
    	call([vars.adb_path + "adb", "shell", "pm", "uninstall", vars.apks[apk_var_name]['package']])


def unlock():
	swipe("259", "665", "533", "702")


def android_wait(time):
	call([vars.adb_path + "adb", "shell", "sleep", time])


def start_app(name):
	call([vars.adb_path + "adb", "shell", "am", "start", "-n", name])


def home():
	call([vars.adb_path + "adb", "shell", "input", "keyevent", "3"])


def menu():
    call([vars.adb_path + "adb", "shell", "input", "keyevent", "1"])


def back():
    call([vars.adb_path + "adb", "shell", "input", "keyevent", "4"])


def task_mgr():
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "1", "172", "1"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "0", "0", "0"])
	android_wait("1")
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "1", "172", "0"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "0", "0", "0"])


def close_first_app():
	task_mgr()
	swipe("503", "879", "286", "878")
	back()


def close_all():
	task_mgr()
	press("502", "983")
	home()


def scroll():
	swipe("248", "837", "255", "396")


def type_text(text, eol=False):
    call([vars.adb_path + "adb", "shell", "input", "text", text])

    if eol is True:
    	call([vars.adb_path + "adb", "shell", "input", "keyevent", "66"])


def type_text_spaces(text_arr, eol):
    for text in text_arr:
        call([vars.adb_path + "adb", "shell", "input", "text", text])
        call([vars.adb_path + "adb", "shell", "input", "keyevent", "62"])

    if eol is True:
        call([vars.adb_path + "adb", "shell", "input", "keyevent", "66"])


def press(x, y):
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "1800"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "53", x])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "54", y])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
	call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])


def long_press(x, y):
	press(x, y)
	android_wait("3")


def swipe(x_start, y_start, x_end, y_end):
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "1800"])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "53", x_start])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "54", y_start])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "53", x_end])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "54", y_end])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
    call([vars.adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
