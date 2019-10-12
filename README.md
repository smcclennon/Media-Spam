# Media-Spam
A personal script I created just to see if I could do it.

This script has no console window and will open a configurable list of URL's and media files (.mp4, .mp3, .jpg, .png) continuously with no easy way to stop the process other than logging out or shutting down the computer.

Features:
- Configure URL's to open in memes.txt
- Configure media to open by simply placing it in the current-working-directory of the script
- No Console Window!
- Confirmations through popups
- Cleanup Script (reset.pyw) [Removes media folder in user-home]

**Notices:**
- This script will leave a folder named 'média' in your user-home directory with all of the media files used on the prior execution of the script. To remove this, run 'reset.pyw'
- CPU and RAM usage will continue to increase until this script is stopped (as browser tabs and media files will continue to be opened)
- There is no easy way to stop this script, that is how it was designed. To stop it, you will need to kill it (via taskmanager for example), or sign out, or shutdown/restart the computer to stop the script

View [Media Spam Releases](https://github.com/smcclennon/Media-Spam/releases)

Requirements:
- Run this script from a usb
- Python 3+ (On a USB* or on the target machine)
- Windows

*If you are planning to use a python install from the USB, please create a shortcut to run the script using Python on the USB

Stage 1 Popup

![Popup 1](https://i.imgur.com/HfaCvMo.png)

Stage 2 Popup

![Popup 2](https://i.imgur.com/DwWVnUH.png)

Error Popup (if the script fails to import one or more libraries

![Error 1](https://i.imgur.com/O7FBzL8.png)

Written in Python 3.7.4 on Windows 10
