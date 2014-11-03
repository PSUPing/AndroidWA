import adb_common
import vars


def play_cc():
	adb_common.apk_inst_chk('CC')
	adb_common.start_app(vars.apks['CC']['package'] + '/' + vars.apks['CC']['launch'])
	adb_common.android_wait("30")
	adb_common.press("335", "555")
	adb_common.android_wait("5")
	adb_common.press("292", "773")
	adb_common.android_wait("5")
	adb_common.press("361", "651")
	adb_common.android_wait("5")
	adb_common.swipe("459", "475", "330", "469")
	adb_common.android_wait("1")
	adb_common.swipe("328", "534", "325", "629")
	adb_common.android_wait("1")
	adb_common.swipe("377", "334", "519", "347")
	adb_common.android_wait("1")
	adb_common.swipe("208", "402", "231", "338")
	adb_common.android_wait("1")
	adb_common.swipe("255", "401", "260", "497")
	adb_common.android_wait("1")
	adb_common.swipe("265", "544", "266", "540")
	adb_common.android_wait("1")
	adb_common.swipe("326", "481", "403", "488")
	adb_common.home()

