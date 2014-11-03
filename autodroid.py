import datetime, random, sys
import vars, adb_common, stat_ops
import candycrush, checkmail, chrome, facebook, googleplus
import netflix, pvz, skype, tetris, zillow 

# Pull the path of the "adb" command
if len(sys.argv) > 3:
    vars.adb_path = sys.argv[2]

# Length of time the automation process should run
start_time = datetime.datetime.now()
curr_time = start_time
end_time = start_time + datetime.timedelta(minutes=2)
#end_time = start_time + datetime.timedelta(hours=3)

# Variable Inits
play_tetris = 0
use_chrome = 0
use_googleplus = 0
close_app = 0
off_and_on = 0
email = 0
play_pvz = 0
play_cc = 0
uninst_tetris = 0
use_netflix = 0
use_facebook = 0
use_skype = 0
use_zillow = 0


# Wake the device up
adb_common.power()
adb_common.unlock()

# This handles if there is a run being done with StatCollector
if len(sys.argv) > 2:
    stat_ops.start_run(sys.argv[1])

while curr_time <= end_time:
    curr_time = datetime.datetime.now()

    rand_num = random.randrange(0, 13000, 1)

    if rand_num < 1000:                                         # Play Tetris
        tetris.play_tetris()
        play_tetris =+ 1
    elif 1000 <= rand_num < 2000:                               # Use Chrome
        chrome.use_chrome()
        use_chrome =+ 1
    elif 2000 <= rand_num < 3000:                               # Use Google+
        googleplus.use_plus()
        use_googleplus =+ 1
    elif 3000 <= rand_num < 4000:                               # Close all open apps
        adb_common.close_all()
        close_app =+ 1
    elif 4000 <= rand_num < 5000:                               # Have you tried turning it off and on?
        adb_common.android_wait("3")
        adb_common.home()
        adb_common.power()
        adb_common.android_wait("15")
        adb_common.power()
        adb_common.unlock()
        off_and_on =+ 1
    elif 5000 <= rand_num < 6000:                               # Check email
        checkmail.check_mail()
        email =+ 1
    elif 6000 <= rand_num < 7000:                               # Play Plants vs Zombies
        pvz.play_pvz()
        play_pvz =+ 1
    elif 7000 <= rand_num < 8000:                               # Play Candy Crush
        candycrush.play_cc()
        play_cc =+ 1
    elif 8000 <= rand_num < 9000:                               # Uninstall Tetris
        adb_common.apk_uninst('Tetris')
        uninst_tetris =+ 1
    elif 9000 <= rand_num < 10000:                              # Use Netflix
        netflix.use_netflix()
        use_netflix =+ 1
    elif 10000 <= rand_num < 11000:                             # Use Facebook
        facebook.use_fb()
        use_facebook =+ 1
    elif 11000 <= rand_num < 12000:                             # Use Skype
        skype.use_skype()
        use_skype =+ 1
    elif 12000 <= rand_num < 13000:                             # Use Zillow
        zillow.use_zillow()
        use_zillow =+ 1


# This handles ending a run being done with StatCollector
if len(sys.argv) > 2:
    stat_ops.stop_run()

# Uninstall all the installed apps to bring it back to original config
for app_name, app_details in vars.apks.iteritems():
    if app_details['uninstall'] is True:
        print "Uninstalling: " + app_name
        adb_common.apk_uninst(app_name)

# Output statistics for this run
print "Played Tetris: " + str(play_tetris)
print "Used Chrome: " + str(use_chrome)
print "Used Google+: " + str(use_googleplus)
print "Closed an app: " + str(close_app)
print "Turned off and on: " + str(off_and_on)
print "Used Email: " + str(email)
print "Played PvZ: " + str(play_pvz)
print "Played Candy Crush: " + str(play_cc)
print "Uninstalled Tetris: " + str(uninst_tetris)
print "Used Netflix: " + str(use_netflix)
print "Used Facebook: " + str(use_facebook)
print "Used Skype: " + str(use_skype)
print "Used Zillow: " + str(use_zillow)

# Close everything and power down the device
adb_common.android_wait("5")
adb_common.close_all()
adb_common.power()
