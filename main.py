import webbrowser
import serial
import keyboard
import sys
import psutil
import os
import subprocess
import serial.tools.list_ports


def main ():
    new = 2
    list = psutil.pids()
    game = input("Enter the video game you're going to play (Keep in mind capitalization and spacing): ")
    game = game + ".exe"
    print(game)

    # myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
    arduino = serial.Serial('COM3', 9600, timeout=20)# You will have to change from where the Arduino is listening to, COM3 or COM4 or /dev/ttyS6 for Linux
    # chrome_path= "/mnt/c/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    # print("port open")
    data = arduino.readline()# the last bit gets rid of the new-line chars


    if (not data is None):

        for i in range(0, len(list)):                # runs through the list of running programs 
            try:
                p = psutil.Process(list[i])
                if p.cmdline()[0].find(game) !=  -1: # checks if the user's game is running
                     p.kill()                        # closes the game
                     print("Ending the fun. Look busy quickly!")
                     break;
            except:
                pass
        
        #print(data.decode('utf-8'))
        #webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path),1)
        #webbrowser.open_new_tab('www.google.com')
        
        keyboard.press_and_release('win + m')                 # command to close all windows in Windows
        keyboard.press_and_release('option + h + m')          # command to close all windows in macOS
        url = "https://www.arduino.cc/en/main/docs"           # to make you look busy
        url2 = "https://docs.python.org/3/library/index.html" # extra busy with python
        url3 = "https://www.arduino.cc/reference/en/"         # extra referenece

        webbrowser.open(url,new=new)
        webbrowser.open(url2,new=new)
        webbrowser.open(url3,new=new)
        
if __name__ == "__main__":
    main()
