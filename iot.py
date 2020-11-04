import webbrowser
import serial
import keyboard
import sys
import psutil
import os
import subprocess

new = 2                 # for urls
list = psutil.pids()    # gets list of all running processes

game = input("Enter the video game you're going to play (Keep in mind capitalization and spacing): ")
game = game + ".exe"

for i in range(0, len(list)):               # runs through the list of running programs 
    try:
        p = psutil.Process(list[i])
        if p.cmdline()[0].find(game) !=  -1:# checks if the user's game is running
            p.kill()                        # closes the game
            print("Ending the fun. Look busy quickly!")
            break;
    except:
        pass


keyboard.press_and_release('win + m')                 # command to close all windows in Windows
keyboard.press_and_release('option + h + m')          # command to close all windows in macOS
url = "https://www.arduino.cc/en/main/docs"           # to make you look busy
url2 = "https://docs.python.org/3/library/index.html" # extra busy with python
url3 = "https://www.arduino.cc/reference/en/"         # extra referenece

webbrowser.open(url,new=new)
webbrowser.open(url2,new=new)
webbrowser.open(url3,new=new)
