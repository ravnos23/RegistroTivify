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

# --- CONFIGURACIÓN ESTRICTA ---
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.0
android.accept_sdk_license = True
# Quitamos el skip_update para que, si falta algo, sepa dónde buscar, 
# pero le estamos dando todo pre-instalado.
android.skip_update = False
