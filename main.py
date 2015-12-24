import serial,os,math

#reads serial port
ser = serial.Serial('com7', 9600)
ser.readline()

referentie = {"A": "skype.exe", "B": "chrome.exe", "C": "vlc.exe", "D": "steam.exe"}
setVolume = {"A": 0, "B": 0, "C": 0, "D": 0}

while 1:
    serialreading = ser.readline()
    serialVolume = float(serialreading[1:])/1024.0
    slider = serialreading[0]
    
    if serialVolume != setVolume[slider]:
        os.system("nircmd setappvolume %s %f" %(referentie[slider], serialVolume))
        setVolume[slider] = serialVolume
