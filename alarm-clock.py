import time, datetime, os, signal, sys 
import vlc
import flipanimation
# Block to kill the alarm if need to be aborted in the middle
if (sys.argv[1]=='c'):
    # Contains the log file with the pid of the alarm script
    with open ('log.txt', "r") as f:
        content = int(f.readline())
        # Sends the kill Signal to the process and then kill itself.
        os.kill(content, signal.SIGKILL)
    os.kill(os.getpid(), signal.SIGKILL)
def current_time():
    """
    Returns the current time in Hour:Minute:Second format after
    extracting it from datetime output.

    Returns:
        [int]: [returns the whole time merged in integer format]
    """
    date_time = datetime.datetime.strptime(str(datetime.datetime.now())[:-7], "%Y-%m-%d %H:%M:%S")
    this_time = int(date_time.strftime("%H%M%S"))
    return this_time
with open('log.txt', "w") as f:
    # Writes the pid for the process in the log file. to be aborted if needed.
    f.write(str(os.getpid()))
temp = sys.argv[1]
if len(temp)>2:
    # To check if the alarm time is given or timer is being set.
    a = datetime.datetime.strptime(temp+" 00", "%H%M %S")
    a = int(a.strftime("%H%M%S"))
else:
    # if timer is set, max value under 60, input is converted to time accordingly
    temp = int(temp)
    if temp>59:
        print("Timer can't be set for more than 60 mins.")
    else:
        curmin = int(str(current_time())[2:4])
        if curmin+temp>60:
            a = current_time()+temp*100
            a = a-6000
            a = a+10000
        else:
            a = current_time()+temp*100
temp = str(a)
val = str(f'Alarm has been set! for {temp[:2]}:{temp[2:4]}:{temp[4:]}')
while True:
    # waiting for the time to be greater than the set time.
    if a>current_time():
        flipanimation.runner(val)
        continue
    else:
        player = vlc.MediaPlayer("/home/anant/Downloads/alarm_clock.mp3")
        for i in range(9):
            player.play()
            time.sleep(5)
            player.stop()
        os.kill(os.getpid(), signal.SIGKILL)
        break