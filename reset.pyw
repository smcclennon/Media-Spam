#Remove média folder from user-home
import shutil; from pathlib import Path; from ctypes import windll
try:
    shutil.rmtree(str(Path.home())+'\\média')
    windll.user32.MessageBoxW(0, "Successfully cleaned user home!\nDeleted: "+str(Path.home())+"\\média\n", "Media Spam: Reset ", 0)
except:
    windll.user32.MessageBoxW(0, "Error: Unable to clean user home. Already clean?", "Media Spam: Reset ", 0)