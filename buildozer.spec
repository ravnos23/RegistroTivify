[app]
title = MiApp
package.name = miapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
android.permissions = INTERNET
android.archs = arm64-v8a

# Configuración obligatoria para evitar errores de descarga en CI
android.skip_update = True
android.sdk = 33
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
