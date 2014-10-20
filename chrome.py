from subprocess import call
import adb_common

def use_chrome(adb_path):
	adb_common.start_app(adb_path, "com.android.chrome/com.google.android.apps.chrome.Main")
	adb_common.android_wait(adb_path, "3")
	adb_common.press(adb_path, "406", "95")
	adb_common.android_wait(adb_path, "2")
	adb_common.type_text_spaces(adb_path, ["nfl", "draft"], True)
	adb_common.android_wait(adb_path, "2")
	adb_common.press(adb_path, "492", "214")
	adb_common.android_wait(adb_path, "2")
	adb_common.back(adb_path)
	adb_common.home(adb_path)
