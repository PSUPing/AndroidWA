from subprocess import call
import sys

# Path to ADB
# Linux
adb_path = "/lib/android/sdk/platform-tools/"
aapt_path = "/lib/android/sdk/build-tools/android-4.4W/"
# Mac
#adb_path = "/Library/Android/sdk/platform-tools/"
#aapt_path = "/Library/Android/sdk/build-tools/19.0.1/"

if len(sys.argv) > 3:
    adb_path = sys.argv[2]

name = sys.argv[1].lower()
apk_name = ''
apk_file_name = ''
pkg_name = ''
act_name = ''

# Get APK Name
p = open('packages.list', 'w')
call([adb_path + "adb", "shell", "pm", "list", "packages", "-f"], stdout=p)
p.close()

adb_events = open('packages.list', 'r')

# Find the APK
for line in adb_events:
    if name in line.lower():
        part1 = line.split(':')
        part2 = part1[1].split('=')
        apk_file_name = part2[0]
        pkg_name = part2[1]

# Get the APK
call([adb_path + "adb", "pull", apk_file_name])

apk_temp = apk_file_name.split('/')
apk_name = apk_temp[len(apk_temp)-1]

# Get Badging Info
b = open(name + ".badging", "w")
call([aapt_path + "aapt", "dump", "badging", apk_name], stdout=b)
b.close()

aapt_badging = open(name + ".badging", "r")

for line in aapt_badging:
    if "launchable-activity" in line.lower():
        part1 = line.split('\'')
        act_name = part1[1]

# Clean up files
call(["rm", "packages.list"])
call(["rm", name + ".badging"])

print "\t# " + name
print "\t\'" + name + "\': {"
print "\t\t\'path\': \'" + apk_name + "\',"
print "\t\t\'package\': \'" + pkg_name.strip() + "\',"
print "\t\t\'launch\': \'" + act_name + "\',"
print "\t\t\'installed\': False,"
print "\t\t\'uninstall\': True"
print "\t},"
