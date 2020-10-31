import webbrowser
import serial
import keyboard
import sys

new=2
keyboard.press_and_release('win + m')#command to close all windows in Windows
keyboard.press_and_release('option + h + m')#command to close all windows in macOS
url="https://www.arduino.cc/en/main/docs"
webbrowser.open(url,new=new)