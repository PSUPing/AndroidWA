# Path to ADB
adb_path = "/lib/android/sdk/platform-tools/"
#adb_path = "/Library/Android/sdk/platform-tools/"

# All the APKs
apks = {
# ------------------------------ Games -----------------------------

    # Tetris
    'Tetris': {
        'path': '/home/drexelping/android_apps/games/com.appmobilegame.tetris-1.apk',
        'package': 'com.appmobilegame.tetris',
        'launch': 'com.peafone.tetrominos.Main',
        'installed': False,
        'uninstall': True
    },

    # Plants vs Zombies
    'PvZ': {
        'path': '/home/drexelping/android_apps/games/com.ea.game.pvz2_na-1.apk',
        'package': 'com.ea.game.pvz2_na',
        'launch': 'com.popcap.PvZ2.PvZ2GameActivity',
        'installed': False,
        'uninstall': True
    },

    # Candy Crush
    'CC': {
        'path': '/home/drexelping/android_apps/games/com.king.candycrushsaga-1.apk',
        'package': 'com.king.candycrushsaga',
        'launch': 'com.king.candycrushsaga.CandyCrushSagaActivity',
        'installed': False,
        'uninstall': True
    },

# ------------------------------ Social -----------------------------

    # Facebook
    'facebook': {
        'path': '/home/drexelping/android_apps/social/com.facebook.katana-1.apk',
        'package': 'com.facebook.katana',
        'launch': 'com.facebook.katana.LoginActivity',
        'installed': True,
        'uninstall': False
    },

    # LinkedIn
    'LinkedIn': {
        'path': '/home/drexelping/android_apps/social/com.linkedin.android-1.apk',
        'package': 'com.linkedin.android',
        'launch': 'com.linkedin.android.authenticator.LaunchActivity',
        'installed': True,
        'uninstall': False
    },

# --------------------------- Entertainment --------------------------

    # Netflix
    'Netflix': {
        'path': '/home/drexelping/android_apps/entertainment/com.netflix.mediaclient-1.apk',
        'package': 'com.netflix.mediaclient',
        'launch': 'com.netflix.mediaclient.LaunchActivity',
        'installed': True,
        'uninstall': False
    },

    # Zillow
    'Zillow': {
        'path': '/home/drexelping/android_apps/realestate/com.zillow.android.zillowmap-1.apk',
        'package': 'com.zillow.android.zillowmap',
        'launch': 'com.zillow.android.zillowmap.ui.apphomescreen.HomeScreenActivity',
        'installed': True,
        'uninstall': False
    },

# --------------------------- Communication --------------------------

    # Skype
    'Skype': {
        'path': '/home/drexelping/android_apps/communication/com.skype.raider-1.apk',
        'package': 'com.skype.raider',
        'launch': 'com.skype.raider.LaunchActivity',
        'installed': True,
        'uninstall': False
    },

# ------------------------------ Sensors -----------------------------

    # Stat Collector
    'StatColl': {
        'path': '/home/drexelping/android_apps/examiner/edu.drexel.StatCollector-3.apk',
        'package': 'edu.drexel.StatCollector',
        'launch': 'edu.drexel.StatCollector.StatViewActivity',
        'installed': True,
        'uninstall': False
    },

# ------------------------ Pre-installed apps ------------------------

    # GMail
    'GMail': {
        'package': 'com.google.android.gm',
        'launch': 'com.google.android.gm.ui.MailActivityGmail',
        'installed': True,
        'uninstall': False
    },

    # Chrome
    'Chrome': {
        'package': 'com.android.chrome',
        'launch': 'com.google.android.apps.chrome.Main',
        'installed': True,
        'uninstall': False
    },

    # Google+
    'GooglePlus': {
        'package': 'com.google.android.apps.plus',
        'launch': 'com.google.android.apps.plus.phone.HomeActivity',
        'installed': True,
        'uninstall': False
    }
}
