[app]
# Título de la aplicación
title = HolaMundo

# Nombre del paquete (debe ser único, usa letras minúsculas)
package.name = holamundo

# Dominio del paquete (puede ser org.test o similar)
package.domain = org.test

# Directorio donde está main.py ('.' indica el directorio actual)
source.dir = .

# Extensiones de archivos a incluir
source.include_exts = py,png,jpg,kv,atlas

# Archivos o patrones a incluir (si tienes recursos adicionales)
source.include_patterns = 

# Archivos o patrones a excluir
source.exclude_exts = spec
source.exclude_dirs = tests, bin, venv
source.exclude_patterns = license, *.md

# Versión de la aplicación
version = 1.0

# Requerimientos de Python (incluye kivy y python3)
requirements = python3,kivy

# Orientación de la pantalla (portrait, landscape o all)
orientation = portrait

# Permisos de Android (agrega solo los necesarios, en este caso ninguno)
android.permissions = 

# Arquitectura de Android (arm64-v8a es común para dispositivos modernos)
android.archs = arm64-v8a

# Versión mínima de la API de Android
android.api = 31

# Versión del NDK de Android (19c es estable para Kivy)
android.ndk = 23b

# Modo de compilación (debug para pruebas, release para producción)
android.release_artifact = apk

# (str) Nombre del archivo de icono (relativo a source.dir)
# icon.filename = %(source.dir)s/icon.png

# (str) Nombre del archivo de presplash (pantalla de carga)
# presplash.filename = %(source.dir)s/presplash.png

# Configuración de Buildozer
[buildozer]
# Directorio para logs
log_level = 2
warn_on_root = 1

# Directorio donde se almacenan las descargas del SDK/NDK
# (puedes dejarlo por defecto)
# android.ndk_path = 
# android.sdk_path = 
# android.ant_path =
