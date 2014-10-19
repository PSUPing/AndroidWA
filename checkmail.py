from subprocess import call
import adb_common

def start_mail(adb_path):
	adb_common.start_app(adb_path, "com.google.android.gm/com.google.android.gm.ui.MailActivityGmail")
	adb_common.android_wait(adb_path, "3")

def search_mail(adb_path):
	adb_common.press(adb_path, "553", "63")
	adb_common.type_text(adb_path, "amazon")
	adb_common.android_wait(adb_path, "2")
	adb_common.back(adb_path)
	adb_common.android_wait(adb_path, "2")

def refresh(adb_path):
	adb_common.swipe(adb_path, "318", "342", "356", "992")

def check_mail(adb_path):
	start_mail(adb_path)
	search_mail(adb_path)
	refresh(adb_path)
	adb_common.android_wait(adb_path, "2")
	adb_common.home(adb_path)
