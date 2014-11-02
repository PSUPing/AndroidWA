import adb_common
import vars


def play_cc():
    adb_common.apk_inst_chk('CC')
    adb_common.start_app(vars.apks['CC']['package'] + '/' + vars.apks['CC']['launch'])