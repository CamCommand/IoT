import webbrowser
import serial


def main ():
    arduino = serial.Serial('COM6', 9600, timeout=.1)
    while True:
    	data = arduino.readline()[:-2] #the last bit gets rid of the new-line chars
	if data:
		print data
webbrowser.open_new_tab('www.google.com')

if __name__ == "__main__":
    main()
    # print(webbrowser.open('www.google.com'))