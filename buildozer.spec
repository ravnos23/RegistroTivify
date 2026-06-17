[app]
title = MiApp
package.name = miapp
package.domain = org.test
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
android.permissions = INTERNET
android.archs = arm64-v8a

# --- LÍNEAS CRÍTICAS PARA QUE NO FALLE ---
android.skip_update = True
android.sdk = 33
android.ndk = 25b
# ------------------------------------------

[buildozer]
log_level = 2
warn_on_root = 1
