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

# IMPORTANTE: Eliminamos las líneas "android.sdk" y "android.skip_update"
# Buildozer 1.6+ detecta y descarga lo que necesita automáticamente.

[buildozer]
log_level = 2
warn_on_root = 1
