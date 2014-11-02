import datetime, random, sys
import vars, adb_common, stat_ops
import checkmail, chrome, googleplus, tetris, pvz, candycrush

# Pull the path of the "adb" command
if len(sys.argv) > 2:
    vars.adb_path = sys.argv[2]
#else:
#    adb_path = "/lib/android/sdk/platform-tools/"

# Length of time the automation process should run
start_time = datetime.datetime.now()
curr_time = start_time
end_time = start_time + datetime.timedelta(minutes=2)
#end_time = start_time + datetime.timedelta(hours=3)

adb_common.power()
adb_common.unlock()

# This handles if there is a run being done with StatCollector
if len(sys.argv) > 3:
    stat_ops.start_run(sys.argv[2])

while curr_time <= end_time:
    curr_time = datetime.datetime.now()

    rand_num = random.randrange(0, 9000, 1)

    if rand_num < 1000:                                         # Play Tetris
        tetris.play_tetris()
    elif 1000 <= rand_num < 2000:                               # Use Chrome
        chrome.use_chrome()
    elif 2000 <= rand_num < 3000:                               # Use Google+
        googleplus.use_plus()
    elif 3000 <= rand_num < 4000:                               # Close all open apps
        adb_common.close_all()
    elif 4000 <= rand_num < 5000:                               # Have you tried turning it off and on?
        adb_common.android_wait("3")
        adb_common.home()
        adb_common.power()
        adb_common.android_wait("15")
        adb_common.power()
        adb_common.unlock()
    elif 5000 <= rand_num < 6000:                               # Check email
        checkmail.check_mail()
    elif 6000 <= rand_num < 7000:                               # Play Plants vs Zombies
        pvz.play_pvz()
    elif 7000 <= rand_num < 8000:                               # Play Candy Crush
        candycrush.play_cc()
    elif 8000 <= rand_num < 9000:                               # Uninstall PvZ
        adb_common.apk_uninst(vars.apks['PvZ']['package'])


# This handles ending a run being done with StatCollector
if len(sys.argv) > 2:
    stat_ops.stop_run()

# Uninstall all the installed apps to bring it back to original config
for app in vars.apks:
    if app['uninstall'] is True:
        adb_common.apk_uninst(app['package'])

# Close everything and power down the device
adb_common.android_wait("5")
adb_common.close_all()
adb_common.power()