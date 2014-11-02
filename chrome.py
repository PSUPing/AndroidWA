import adb_common
import vars


def use_chrome():
#    adb_common.start_app(adb_path, "com.android.chrome/com.google.android.apps.chrome.Main")
    adb_common.start_app(vars.apks['Chrome']['package'] + '/' + vars.apks['Chrome']['launch'])
    adb_common.android_wait("3")
    adb_common.press("406", "95")
    adb_common.android_wait("2")
    adb_common.type_text_spaces(["nfl", "draft"], True)
    adb_common.android_wait("2")
    adb_common.press("492", "214")
    adb_common.android_wait("2")
    adb_common.back()
    adb_common.home()
