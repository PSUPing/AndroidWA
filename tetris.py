import adb_common
import vars


def play_tetris():
    adb_common.apk_inst_chk('Tetris')
    adb_common.start_app(vars.apks['Tetris']['package'] + '/' + vars.apks['Tetris']['launch'])
    adb_common.android_wait("4")
    adb_common.press("326", "363")
    adb_common.press("105", "469")
    adb_common.android_wait("15")
    adb_common.swipe("315", "330", "316", "501")
    adb_common.android_wait("2")
    adb_common.home()
