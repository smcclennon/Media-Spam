#Media Spam
ver='1.2.0'
#github.com/smcclennon/Media-Spam


try:
    from ctypes import windll
    import glob,webbrowser,shutil,random; from pathlib import Path
    windll.user32.MessageBoxW(0, "Stage 1/2\nLibraries successfully imported!\nPress OK to begin loading media\nDon't unplug your USB yet! You will recieve another popup when it is safe to do so", "Media Spam v"+str(ver), 0)
except:
    windll.user32.MessageBoxW(0, "Error: Failed to import one or more requirements.\nVisit github.com/smcclennon/Media-Spam for support", "Media Spam: v"+str(ver), 0)
    exit()


z = str(Path.home()) #Get windows home DIR (copy files here)


#Create a new media folder
try:
    shutil.rmtree(z+'\\média') #Try to delete the media folder if it already exists
except:
    pass
Path(z+'\\média').mkdir(parents=True, exist_ok=True) #Create the media folder
windll.kernel32.SetFileAttributesW(z+'\\média', 2)


#Copy over media files from the current-working-directory to user-home/média
for filename in glob.glob('*.mp4'): #user-home example: 'C:\Users\John'
    shutil.copy(str(filename),str(z)+'\\média\\')
for filename in glob.glob('*.mp3'):
    shutil.copy(str(filename),str(z)+'\\média\\')
for filename in glob.glob('*.jpg'):
    shutil.copy(str(filename),str(z)+'\\média\\')
for filename in glob.glob('*.png'):
    shutil.copy(str(filename),str(z)+'\\média\\')
for filename in glob.glob('*.mov'):
    shutil.copy(str(filename),str(z)+'\\média\\')


try:
    with open('memes.txt', 'r') as f:
        y=f.read().split('\n') #Load each line from memes.txt to variable y
except: #if there is a problem with memes.txt create a new one
    f=open('memes.txt', 'w')
    f.write('http://www.partridgegetslucky.com/\n')
    f.write('https://omfgdogs.com/\n')
    f.write('http://heeeeeeeey.com/\n')
    f.write('http://cat-bounce.com/\n')
    f.write('http://dogs.are.the.most.moe/\n')
    f.write('http://chihuahuaspin.com/\n')
    f.write('http://burymewithmymoney.com/\n')
    f.write('http://corndog.io/\n')
    f.write('http://beesbeesbees.com/')
    f.close()
    with open('memes.txt', 'r') as f:
        y=f.read().split('\n') #Load each line in memes.txt variable y


a=[]
c=[]
for b in y: #for URL in y, append to array c
    c.append(str(b))
for b in glob.glob('*.mp4'): #Load media files from user-home into array a
    a.append(str(b))
for b in glob.glob('*.mp3'):
    a.append(str(b))
for b in glob.glob('*.jpg'):
    a.append(str(b))
for b in glob.glob('*.png'):
    a.append(str(b))
for b in glob.glob('*.mov'):
    a.append(str(b))


if a==[]: #if no media files were found
    media=0
    windll.user32.MessageBoxW(0, "Stage 2/2\nError: No media found! URL's from memes.txt will still be opened.\nVisit github.com/smcclennon/Media-Spam for support\nPress OK to continue", "Media Spam v"+str(ver), 0)
else:
    media=1
    windll.user32.MessageBoxW(0, "Stage 2/2\nMedia loaded! You can now disconnect your USB\nPress OK to begin", "Media Spam v"+str(ver), 0)


while True:
    if media==1:
        webbrowser.open(str(z)+'\\média\\'+str(random.choice(a))) #Open a random media file (mp4, png etc) from array a
    webbrowser.open(str(random.choice(c))) #Open a random URL from array c