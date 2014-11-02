import adb_common
import vars


def use_plus():
#    adb_common.start_app(adb_path, "com.google.android.apps.plus/com.google.android.apps.plus.phone.HomeActivity")
    adb_common.start_app(vars.apks['GooglePlus']['package'] + '/' + vars.apks['GooglePlus']['launch'])
    adb_common.android_wait("3")
    adb_common.scroll()
    adb_common.scroll()
    adb_common.scroll()
    adb_common.home()
