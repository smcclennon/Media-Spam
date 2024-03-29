# Media-Spam
A personal script I created just to see if I could do it.

This script has no console window and will open a configurable list of URL's and media files (.mp4, .mov, .mp3, .png, .jpg) continuously with no easy way to stop the process other than logging out or shutting down the computer.

# Features
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

# Installation
- Unzip items in Media-Spam.zip to the same location (preferably a USB)
- Customise 'memes.txt' with URL's of your choice (to open)
- Customise media files (.mp4 .mov .mp3 .png .jpg) in the folder where 'media.pyw' is to the files of your choice (to open)
- Run the script (preferably from a USB)

Requirements:
- Run this script from a usb
- Python 3+ (On a USB* or on the target machine)
- Windows

*If you are planning to use a python install from the USB, please create a shortcut to run the script using Python on the USB

# Screenshots
Stage 1 Popup

![Popup 1](https://i.imgur.com/HfaCvMo.png)

Stage 2 Popup

![Popup 2](https://i.imgur.com/DwWVnUH.png)

Import Error Popup (if the script fails to import one or more libraries

![Error 1](https://i.imgur.com/O7FBzL8.png)

Media Load Error Popup

![Error 2](https://i.imgur.com/qlbBecd.png)

**reset.pyw** Success

![Success](https://i.imgur.com/2dzYc1m.png)

**reset.pyw** Error

![Error](https://i.imgur.com/YseezFs.png)

Written in Python 3.7.4 on Windows 10
