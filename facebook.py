import adb_common
import vars


def use_fb():
    adb_common.apk_inst_chk('facebook')
    adb_common.start_app(vars.apks['facebook']['package'] + '/' + vars.apks['facebook']['launch'])
    adb_common.android_wait("6")
    adb_common.scroll()
    adb_common.scroll()
    adb_common.scroll()
    adb_common.home()
