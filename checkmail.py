import adb_common
import vars


def start_mail():
#    adb_common.start_app(adb_path, "com.google.android.gm/com.google.android.gm.ui.MailActivityGmail")
    adb_common.start_app(vars.apks['GMail']['package'] + '/' + vars.apks['GMail']['launch'])
    adb_common.android_wait("3")


def search_mail():
    adb_common.press("553", "63")
    adb_common.type_text("amazon")
    adb_common.android_wait("2")
    adb_common.back()
    adb_common.android_wait("2")


def refresh():
    adb_common.swipe("318", "342", "356", "992")


def check_mail():
    start_mail()
    search_mail()
    refresh()
    adb_common.android_wait("2")
    adb_common.home()
