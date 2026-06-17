[app]
title = MiApp
package.name = miapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# Solo lo básico. Si esto funciona, iremos añadiendo tus librerías una a una.
requirements = python3,kivy
android.permissions = INTERNET
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
