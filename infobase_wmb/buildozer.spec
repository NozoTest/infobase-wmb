[app]

# Título de tu app (puedes cambiarlo)
title = Infobase WMB

# Nombre del paquete (NO usar espacios ni tildes)
package.name = infobasewmb

# Nombre de dominio (cámbialo si quieres)
package.domain = org.infobase

# Versión de la app (ej: 1.0, 2.0, etc.)
version = 1.0

# Carpeta donde están tus archivos (deja el punto)
source.dir = .

# Requisitos técnicos (¡NO CAMBIES ESTO!)
requirements = python3, kivy==2.1.0, sqlite3, pypdf2, android

# Permisos de Android (para usar internet si es necesario)
android.permissions = INTERNET

# Orientación de la pantalla (vertical)
orientation = portrait

# Evitar pantalla completa (para que se vea como app normal)
fullscreen = 0

# Lanzador de la app (no tocar)
log_level = 2
android.arch = armeabi-v7a