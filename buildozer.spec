[app]
title = MiApp
package.name = miapp
package.domain = org.miapp
source.dir = .
version = 1.0
requirements = 
    python3==3.10.13,
    kivy==2.3.0,
    android
orientation = portrait
fullscreen = 0

# Android
android.api = 34
android.minapi = 21
android.archs = arm64-v8a
android.ndk = $ANDROID_NDK_VERSION
android.sdk_path = $ANDROID_HOME
android.ndk_path = $ANDROID_HOME/ndk/$ANDROID_NDK_VERSION
android.p4a_dir = $HOME/.local/lib/python3.10/site-packages/pythonforandroid

# Build
[buildozer]
log_level = 2
target_dir = bin
warn_on_root = 1