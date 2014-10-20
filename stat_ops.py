from subprocess import call

def start_run(adb_path, run_name):
	adb_common.start_app(adb_path, "edu.drexel.StatCollector/edu.drexel.StatCollector.StatViewActivity")
	adb_common.android_wait(adb_path, "3")
	adb_common.press(adb_path, "351", "104")
	adb_common.android_wait(adb_path, "2")
	adb_common.type_text(adb_path, run_name, False)
	adb_common.press(adb_path, "397", "316")
	adb_common.android_wait(adb_path, "2")
	adb_common.home(adb_path)

def stop_run(adb_path):
	adb_common.start_app(adb_path, "edu.drexel.StatCollector/edu.drexel.StatCollector.StatViewActivity")
	adb_common.android_wait(adb_path, "3")
	adb_common.press(adb_path, "397", "316")
	adb_common.android_wait(adb_path, "2")
	adb_common.home(adb_path)
