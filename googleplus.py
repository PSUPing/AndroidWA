from subprocess import call
import adb_common

def use_plus(adb_path):
	adb_common.start_app(adb_path, "com.google.android.apps.plus/com.google.android.apps.plus.phone.HomeActivity")
	adb_common.android_wait(adb_path, "3")
	adb_common.scroll(adb_path)
	adb_common.scroll(adb_path)
	adb_common.scroll(adb_path)
	adb_common.home(adb_path)
