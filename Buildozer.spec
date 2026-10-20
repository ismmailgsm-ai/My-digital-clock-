
[app]

title = My Digital Clock
package.name = mydigitalclock
package.domain = com.ismmailgsm
source.dir = .
source.include_exts = py,kv,png,jpg,ttf
version = 2.0.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True

[buildozer]

log_level = 2
warn_on_root = 1
