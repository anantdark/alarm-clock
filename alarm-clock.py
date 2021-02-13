import time
import datetime
import os, signal
import vlc
# player = vlc.MediaPlayer("/home/anant/adhiraataudio.mp3")
# for i in range(2):
#     with open('log.txt', "w") as f:
#         f.write(str(os.getpid()))
#     player.play()
#     time.sleep(1)
#     player.stop()
#     os.system('chromium')
#     signal.alarm(1)
#         os.kill(os.getpid, signal.SIGKILL)
a = datetime.datetime.strptime(input()+" 00", "%H %M %S")
a = int(a.strftime("%H%M%S"))
while True:
    b = datetime.datetime.strptime(str(datetime.datetime.now())[:-7], "%Y-%m-%d %H:%M:%S")
    b = int(b.strftime("%H%M%S"))
    if a>b:
        time.sleep(1)
        continue
    else:
        os.system('firefox')
        break
