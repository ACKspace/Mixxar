import os
import pythoncom, pyHook
from pyHook import HookManager
from pyHook.HookManager import HookConstants

def setVolumeActive(event):
    ctrl_pressed = pyHook.GetKeyState(HookConstants.VKeyToID('VK_LCONTROL'))
    alt_pressed = pyHook.GetKeyState(HookConstants.VKeyToID('VK_LMENU'))
    if ctrl_pressed and alt_pressed:
        return do(event)

program = ""
def chooseProgram(event):
    global program
    program1 = event.KeyID
    program2 = event.KeyID
    program3 = event.KeyID
    
    if program1 == 97:
        program = "skype.exe"
    elif program2 == 98:
        program = "chrome.exe"
    elif program3 == 99:
        program = "steam.exe"
    return 

def do(event):
    chooseProgram(event)
    setVolume(event)
    return

def setVolume(event):
    vol_up = event.KeyID
    vol_down = event.KeyID
    if vol_up == 190:
        plus = 0.1
        os.system("nircmd changeappvolume %s %s" %(program, plus))
    elif vol_down == 188:
        minus = -0.1
        os.system("nircmd changeappvolume %s %s" %(program, minus))
    return

hm = pyHook.HookManager()
hm.KeyDown = setVolumeActive
hm.HookKeyboard()
pythoncom.PumpMessages()
