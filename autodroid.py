from subprocess import call
import datetime, random, sys
import apks, adb_common, stat_ops
import checkmail, chrome, googleplus, tetris

# Pull the path of the "adb" command
if (len(sys.argv) > 3):
	adb_path = sys.argv[2]
else:	
	adb_path = "/lib/android/sdk/platform-tools/"

# Length of time the automation process should run
start_time = datetime.datetime.now()
curr_time = start_time
#end_time = start_time + datetime.timedelta(minutes=2)
end_time = start_time + datetime.timedelta(hours=3)

adb_common.power(adb_path)
adb_common.unlock(adb_path)

# This handles if there is a run being done with StatCollector
if len(sys.argv) > 2:
    stat_ops.start_run(adb_path, sys.argv[1])

while (curr_time <= end_time):
	curr_time = datetime.datetime.now()

	rand_num = random.randrange(0, 70000, 1)

	if rand_num < 10000:                          # Install Tetris
		if (apks.apks[2] == False):
			adb_common.apk_inst(adb_path, apks.apks[0])
			apks.apks[2] = True
	elif (rand_num >= 10000 and rand_num < 20000):  # Use Chrome
		chrome.use_chrome(adb_path)
	elif (rand_num >= 20000 and rand_num < 30000):  # Use Google+
		googleplus.use_plus(adb_path)
	elif (rand_num >= 30000 and rand_num < 40000):  # Close all open apps
		adb_common.close_all(adb_path)
	elif (rand_num >= 40000 and rand_num < 50000):  # Play and uninstall Tetris
		if (apks.apks[2] == True):
			tetris.play_tetris(adb_path)
			adb_common.apk_uninst(adb_path, apks.apks[1])
			apks.apks[2] = False
	elif (rand_num >= 50000 and rand_num < 60000):  # Have you tried turning it off and on?
		adb_common.android_wait(adb_path, "3")
		adb_common.home(adb_path)
		adb_common.power(adb_path)
		adb_common.android_wait(adb_path, "15")
		adb_common.power(adb_path)
		adb_common.unlock(adb_path)
	elif (rand_num >= 60000 and rand_num < 70000):  # Check email
		checkmail.check_mail(adb_path)

# This handles ending a run being done with StatCollector
if (len(sys.argv) > 2):
	stat_ops.stop_run(adb_path)

# Close everything and power down the device
adb_common.android_wait(adb_path, "5")
adb_common.close_all(adb_path)
adb_common.power(adb_path)