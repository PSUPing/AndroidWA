import adb_common
import vars


def play_pvz():
    adb_common.apk_inst_chk('PvZ')
    adb_common.start_app(vars.apks['PvZ']['package'] + '/' + vars.apks['PvZ']['launch'])