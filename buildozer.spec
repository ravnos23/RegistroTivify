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

# --- CONFIGURACIÓN DE VERSIONES ESTABLES ---
android.sdk = 33
android.ndk = 25b
# Esto hace que Buildozer acepte la licencia internamente sin errores de "pipe"
android.accept_sdk_license = True
# Permitimos que busque el SDK, pero restringido a la versión 33 que configuramos
android.skip_update = False

[buildozer]
log_level = 2
warn_on_root = 1
