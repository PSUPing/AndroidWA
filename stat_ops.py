import adb_common
import vars


def inst_stat_ops():
    adb_common.apk_inst_chk('StatColl')


def start_run(run_name):
#    adb_common.start_app(adb_path, "edu.drexel.StatCollector/edu.drexel.StatCollector.StatViewActivity")
    adb_common.start_app(vars.apks['StatColl']['package'] + '/' + vars.apks['StatColl']['launch'])
    adb_common.android_wait("3")
    adb_common.press("351", "104")
    adb_common.android_wait("2")
    adb_common.type_text(run_name)
    adb_common.press("397", "200")
    adb_common.android_wait("2")
    adb_common.home()


def stop_run():
#    adb_common.start_app(adb_path, "edu.drexel.StatCollector/edu.drexel.StatCollector.StatViewActivity")
    adb_common.start_app(vars.apks['StatColl']['package'] + '/' + vars.apks['StatColl']['launch'])
    adb_common.android_wait("3")
    adb_common.press("397", "200")
    adb_common.android_wait("2")
    adb_common.home()
