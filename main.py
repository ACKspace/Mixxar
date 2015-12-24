import serial,os,math

#reads serial port
ser = serial.Serial('com7', 9600)
ser.readline()

#initialize the processes and volume for each slider using dictionaries
program = {"A": "", "B": "", "C": "", "D": ""}
setVolume = {"A": 0, "B": 0, "C": 0, "D": 0}

#main loop
while 1:
    #read the serial output and the slider for which the output is given
    serialreading = ser.readline()
    serialVolume = float(serialreading[1:])/1024.0
    slider = serialreading[0]
    
    #set new volume if the slider has changed, constantly adjusting is more resource-heavy
    if serialVolume != setVolume[slider]:
        os.system("nircmd setappvolume %s %f" %(program[slider], serialVolume))
        setVolume[slider] = serialVolume
