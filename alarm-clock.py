import time, datetime, os, signal, vlc, sys
if (sys.argv[1]=='c'):
    with open ('log.txt', "r") as f:
        content = int(f.readline())
        os.kill(content, signal.SIGKILL)
    os.kill(os.getpid(), signal.SIGKILL)
def current_time():
    date_time = datetime.datetime.strptime(str(datetime.datetime.now())[:-7], "%Y-%m-%d %H:%M:%S")
    this_time = int(date_time.strftime("%H%M%S"))
    return this_time
with open('log.txt', "w") as f:
    f.write(str(os.getpid()))
temp = sys.argv[1]
if " " in temp:
    a = datetime.datetime.strptime(temp+" 00", "%H-%M %S")
    a = int(a.strftime("%H%M%S"))
else:
    temp = int(temp)
    if temp>59:
        print("Timer can't be set for more than 60 mins.")
    else:
        a = current_time()+(temp*100)
temp = str(a)
print(f'Alarm has been set! for {temp[:2]}:{temp[2:4]}:{temp[4:]}')
while True:
    if a>current_time():
        time.sleep(1)
        continue
    else:
        player = vlc.MediaPlayer("/home/anant/dusk.mp3")
        for i in range(1):
            player.play()
            time.sleep(30)
            player.stop()
        os.kill(os.getpid(), signal.SIGKILL)
        break