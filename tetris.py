from subprocess import call
import adb_common

def play_tetris(adb_path):
	adb_common.start_app(adb_path, "com.appmobilegame.tetris/com.peafone.tetrominos.Main")
	adb_common.android_wait(adb_path, "4")
	adb_common.press(adb_path, "326", "363")
	adb_common.press(adb_path, "105", "469")
	adb_common.android_wait(adb_path, "15")
	adb_common.swipe(adb_path, "315", "330", "316", "501")
	adb_common.android_wait(adb_path, "2")
	adb_common.home(adb_path)
