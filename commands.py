import pydirectinput as pdi
import os
# schedule module is not included with python
import schedule
import time
import threading
from win32gui import GetWindowText, GetForegroundWindow

# list of events we want
# on start, we want to delay a good 10 seconds to allow for the map to load
# * side note * also want to make sure the correct window is tabbed in some how
# move character forward and left to the spot we would like them to go
# aim towards middle and trigger attack
# wait a few seconds for attack to finish
# open map and travel back: G F E E
# repeat
def script_actions(self):
    try:
        delay = self.delayString.get()
        delay = int(delay)
    except:
        delay = 15
    time.sleep(delay)

    if self.checkVar.get() == 1:

        t_passed = True
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™":
            pdi.keyDown('w')
            time.sleep(3)
            pdi.keyUp('w')
        else:
            t_passed = False
            cancelSchedule(self)
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™" and t_passed is True:
            pdi.keyDown('a')
            time.sleep(.6)
            pdi.keyUp('a')
        else:
            t_passed = False
            cancelSchedule(self)
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™" and t_passed is True:
            pdi.keyDown('w')
            time.sleep(1.5)
            pdi.keyUp('w')
        else:
            t_passed = False
            cancelSchedule(self)
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™" and t_passed is True:
            pdi.press('3')
            time.sleep(4)
        else:
            t_passed = False
            cancelSchedule(self)
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™" and t_passed is True:
            pdi.press('g')
            time.sleep(1)
        else:
            t_passed = False
            cancelSchedule(self)
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™" and t_passed is True:
            pdi.press('f')
            time.sleep(1)
        else:
            t_passed = False
            cancelSchedule(self)
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™" and t_passed is True:
            pdi.press('e')
            time.sleep(1)
        else:
            t_passed = False
            cancelSchedule(self)
        if GetWindowText(GetForegroundWindow()) == "ELDEN RING™" and t_passed is True:
            pdi.press('e')
        else:
            cancelSchedule(self)
    else:
        pdi.keyDown('w')
        time.sleep(3)
        pdi.keyUp('w')
        pdi.keyDown('a')
        time.sleep(.6)
        pdi.keyUp('a')
        pdi.keyDown('w')
        time.sleep(1.5)
        pdi.keyUp('w')
        pdi.press('3')
        time.sleep(4)
        pdi.press('g')
        time.sleep(1)
        pdi.press('f')
        time.sleep(1)
        pdi.press('e')
        time.sleep(1)
        pdi.press('e')

def closeWindow(self):
    # cancelling so that we can free up resources
    cancelSchedule(self)
    os._exit(0)

def startStop(self):
    if self.AutoEnabled is True:
        # cancel the schedule
        cancelSchedule(self)
    else:
        # schedule was cancelled, start it up

        defaultSchedule(self)

def defaultSchedule(self):
    self.setExt['text'] = "Stop"
    self.AutoEnabled = True
    # create a schedule thread and pass frequency
    self.scheduleThread = threading.Thread(target=scheduleThreadFunc, args=(self,))
    self.scheduleThread.start()

def scheduleThreadFunc(self):
    schedule.every(5).seconds.do(script_actions, self)

    while self.AutoEnabled:
        schedule.run_pending()
        time.sleep(5)

def cancelSchedule(self):
    self.setExt['text'] = "Start"
    schedule.clear()
    # setting here to avoid having to call it 20 times
    self.AutoEnabled = False
    # if the thread is alive, we need to kill it
    # quitting the program doesn't auto delete threads
    try:
        if self.scheduleThread.is_alive():
            self.scheduleThread.join()
    except:
        pass

