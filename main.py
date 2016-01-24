import serial,os,math,time

os.system("cls")

#initialize the processes and volume for each slider using dictionaries
program = {"A": "UT2004.exe", "B": "chrome.exe", "C": "telegram.exe", "D": "firefox.exe"}
setVolume = {"A": 0, "B": 0, "C": 0, "D": 0}
ser = ""

def ardConnectionCheck():
    global ser
    #cycle through all available COM ports to poll for a connected device
    #repeats itself if no arduino is found on the COM ports
    print "Connecting to arduino..."
    ports = ['COM%s' % (i + 1) for i in range(256)]
    
    ser = serial.Serial(port, 9600, timeout=2)
    ardFound = False
    while not ardFound:
        for port in ports:
            print "Testing %s" %(port)
            try:
                
                serInput = ser.readline()
                #read only the first 13 characters, as a weird character is being output at the end
                serInput = serInput[0:13]
                timepass = time.clock()
                if serInput != "ARDUINO READY":
                    ser.close()
                else:
                    #connected device found, test if the device is an arduino sending a ready state
                    #if so, break out of the for and while loops
                    print "Connected to arduino on port %s." %(port)
                    ardFound = True
                    #return ready state to the arduino to begin slider configuration
                    ser.write("OS READY")
                    volChange()
                    break
            except (OSError, serial.SerialException):
                pass        
            #reads connection-ok from every line
            serConnection = ser.readline()
            ardCon = serConnection[0:6]

#return ready state to the arduino to begin slider configuration
#ser.write("OS READY")



#main loop
def volChange():
    global ser
    global ardCon
    while 1:
        #read the serial output and the slider for which the output is given
        serialreading = ser.readline()
        serialVolume = float(serialreading[7:])/1024.0
        slider = serialreading[0]
        #connection check
        while ardCon == "CON-OK":
            #set new volume if the slider has changed, constantly adjusting is more resource-heavy
            if serialVolume != setVolume[slider]:
                os.system("nircmd setappvolume %s %f" %(program[slider], serialVolume))
                setVolume[slider] = serialVolume
            #if arduino is disconnected, restart the connection-initializer script
            else: 
                ardConnectionCheck()        


    
        
#starts the progam
ardConnectionCheck()