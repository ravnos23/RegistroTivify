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

# Esto es lo único necesario para que no pregunte nada y sea permisivo
android.accept_sdk_license = True
# Si Buildozer necesita una versión, la bajará él mismo a su carpeta local
android.sdk = 33
android.ndk = 25b
