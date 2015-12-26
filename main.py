import serial,os,math,time

os.system("cls")

#initialize the processes and volume for each slider using dictionaries
processes = {"A": "skype.exe", "B": "chrome.exe", "C": "vlc.exe", "D": "steam.exe"}
setVolume = {"A": 0, "B": 0, "C": 0, "D": 0}

#cycle through all available COM ports to poll for a connected device
#repeats itself if no arduino is found on the COM ports
print "Connecting to arduino..."
ports = ['COM%s' % (i + 1) for i in range(256)]
ardFound = False
while not ardFound:
    for port in ports:
        #print "Testing %s" %(port)
        try:
            ser = serial.Serial(port, 9600)
        except (OSError, serial.SerialException):
            pass        
        else:
            #connected device found, test if the device is an arduino sending a ready state
            #if so, break out of the for and while loops
            serInput = ser.readline()
            #read only the first 13 characters, as a weird character is being output at the end
            serInput = serInput[0:13]
            if serInput != "ARDUINO READY":
                ser.close()
            else:
                print "Connected to arduino on port %s." %(port)
                ardFound = True
                break

#return ready state to the arduino to begin slider configuration
ser.write("OS READY")


'''ser = serial.Serial(port, 9600)
#send ready state back to the arduino to start configuring the sliders
ser.write("OS READY")

while 1:
    print ser.readline()
    time.sleep(1)'''


'''os.system("echo 'Connecting to arduino...'")
ser.write("INIT READY")
x = 1
while ser.readline() != "ARDUINO READY":
    #poll once every second as this more than needed
    os.system("echo 'Attempt %i'" %(x))
    x += 1
    time.sleep(1)
os.system("echo 'Connected!'")'''








'''#start loop to write all sliders to the dictionaries
print "Configuring volume sliders:"
while ser.readline() != "SLIDERS DONE":
	pass

#configuration is done and the script will continue to the main loop after 10 seconds
print "Sliders are configured! Starting in 10..."
time.sleep(10)
os.system("cls")

#main loop
while 1:
    #read the serial output and the slider for which the output is given
    serialreading = ser.readline()
    serialVolume = float(serialreading[1:])/1024.0
    slider = serialreading[0]
    
    #set new volume if the slider has changed, constantly adjusting is more resource-heavy
    if serialVolume != setVolume[slider]:
        os.system("nircmd setappvolume %s %f" %(processes[slider], serialVolume))
        setVolume[slider] = serialVolume'''
