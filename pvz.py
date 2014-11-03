import adb_common
import vars


def play_pvz():
	adb_common.apk_inst_chk('PvZ')
	adb_common.start_app(vars.apks['PvZ']['package'] + '/' + vars.apks['PvZ']['launch'])
	adb_common.android_wait("8")
	adb_common.press("312", "685")
	adb_common.press("285", "668")
	adb_common.press("262", "557")
	adb_common.press("254", "549")
	adb_common.android_wait("2")
	adb_common.apk_inst_chk('Tetris')
	adb_common.start_app(vars.apks['Tetris']['package'] + '/' + vars.apks['Tetris']['launch'])
	adb_common.android_wait("1")
	adb_common.home()
