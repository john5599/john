[app]

# (str) Title of your application
title = WorkAssistant

# (str) Package name
package.name = org.example.workassistant

# (str) Package domain (needed for android/ios packaging)
package.domain = org.example

# (str) Source code where the main.py resides
source.dir = .

# (list) List of resource directories to package (comma separated)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
source.exclude_patterns = license.txt

# (list) List of requirements (comma separated)
requirements = kivy

# (str) Application versioning
version = 1.0

# (list) Application permissions
android.permissions = INTERNET

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# (str) Presplash background color (for Android)
android.presplash_color = #FFFFFF

# (str) Presplash image (for Android)
android.presplash = presplash.png

# (str) Icon of the application
icon.filename = icon.png
