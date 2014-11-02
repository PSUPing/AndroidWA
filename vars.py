# Path to ADB
adb_path = "/lib/android/sdk/platform-tools/"
#adb_path = "/Library/Android/sdk/platform-tools/"

# All the APKs
apks = {
# ------------------------------ Games -----------------------------

    # Tetris
    'Tetris': {
        'path': '~/android_apps/games/com.appmobilegame.tetris-1.apk',
        'package': 'com.appmobilegame.tetris',
        'launch': 'com.peafone.tetrominos.Main',
        'installed': False,
        'uninstall': True
    },

    # Plants vs Zombies
    'PvZ': {
        'path': '~/android_apps/games/com.ea.game.pvz2_na-1.apk',
#        'package': 'com.ea.game.pvz2_na',
#        'launch': 'com.ea.game.pvz2_na',
        'installed': False,
        'uninstall': True
    },

    # Candy Crush
    'CC': {
#        'path': '~/android_apps/games/com.ea.game.pvz2_na-1.apk',
#        'package': 'com.ea.game.pvz2_na',
#        'launch': 'com.ea.game.pvz2_na',
        'installed': False,
        'uninstall': True
    },

# ------------------------------ Social -----------------------------

    # Facebook
    'facebook': {
#        'path': '~/android_apps/social/com.appmobilegame.tetris-1.apk',
        'package': 'com.facebook.katana',
        'launch': 'com.facebook.katana.LoginActivity',
        'installed': True,
        'uninstall': False
    },

    # LinkedIn
    'LinkedIn': {
#        'path': '~/android_apps/games/com.appmobilegame.tetris-1.apk',
#        'package': 'com.appmobilegame.tetris',
#        'launch': 'com.peafone.tetrominos.Main',
        'installed': True,
        'uninstall': False
    },

# ------------------------------ Sensors -----------------------------

    # Stat Collector
    'StatColl': {
#        'path': '~/android_apps/social/com.appmobilegame.tetris-1.apk',
        'package': 'edu.drexel.StatCollector',
        'launch': 'edu.drexel.StatCollector.StatViewActivity',
        'installed': True
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