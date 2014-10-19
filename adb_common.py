from subprocess import call

def power(adb_path):
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "1", "116", "1"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "0", "0", "0"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "1", "116", "0"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event1", "0", "0", "0"])

def apk_inst(adb_path, apk_name):
	call([adb_path + "adb", "install", apk_name])

def apk_uninst(adb_path, pkg_name):
	call([adb_path + "adb", "shell", "pm", "uninstall", pkg_name])

def unlock(adb_path):
	swipe(adb_path, "259", "665", "533", "702")

def android_wait(adb_path, time):
	call([adb_path + "adb", "shell", "sleep", time])

def start_app(adb_path, name):
	call([adb_path + "adb", "shell", "am", "start", "-n", name])

def home(adb_path): 
	call([adb_path + "adb", "shell", "input", "keyevent", "3"])

def menu(adb_path): 
	call([adb_path + "adb", "shell", "input", "keyevent", "1"])

def back(adb_path):
	call([adb_path + "adb", "shell", "input", "keyevent", "4"])

def task_mgr(adb_path):
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "1", "172", "1"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "0", "0", "0"])
	android_wait(adb_path, "1")
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "1", "172", "0"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event7", "0", "0", "0"])

def close_first_app(adb_path):
	task_mgr(adb_path)
	swipe(adb_path, "503", "879", "286", "878")
	back(adb_path)

def close_all(adb_path):
	task_mgr(adb_path)
	press(adb_path, "502", "983")
	home(adb_path)

def scroll(adb_path):
	swipe(adb_path, "248", "837", "255", "396")

def type_text(adb_path, text):
	call([adb_path + "adb", "shell", "input", "text", text])
	call([adb_path + "adb", "shell", "input", "keyevent", "66"])

def type_text_spaces(adb_path, text_arr):
	for text in text_arr:
		call([adb_path + "adb", "shell", "input", "text", text])
		call([adb_path + "adb", "shell", "input", "keyevent", "62"])
	call([adb_path + "adb", "shell", "input", "keyevent", "66"])

def press(adb_path, x, y):
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "1800"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "53", x])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "54", y])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])

def long_press(adb_path, x, y):
	press(adb_path, x, y)
	android_wait(adb_path, "3")

def swipe(adb_path, x_start, y_start, x_end, y_end):
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "1800"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "53", x_start])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "54", y_start])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "53", x_end])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "54", y_end])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "3", "57", "4294967295"])
	call([adb_path + "adb", "shell", "sendevent", "/dev/input/event0", "0", "0", "0"])
