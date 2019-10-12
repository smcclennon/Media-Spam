#Remove média folder from user-home
import shutil; from pathlib import Path
try:
    shutil.rmtree(str(Path.home())+'\\média')
    shutil.rmtree(str(Path.home())+'\\media')
except:
    try:
        shutil.rmtree(str(Path.home())+'\\media')
    except:
        exit
