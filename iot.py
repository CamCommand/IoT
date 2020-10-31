import webbrowser
import serial
import keyboard
import sys

new=2
keyboard.press_and_release('win + m')#command to close all windows in Windows
keyboard.press_and_release('option + h + m')#command to close all windows in macOS
url="https://www.arduino.cc/en/main/docs"# to make you look busy
url2="https://docs.python.org/3/library/index.html"# extra busy with python
url3="https://www.arduino.cc/reference/en/"# extra referenece
webbrowser.open(url,new=new)
webbrowser.open(url2,new=new)
webbrowser.open(url3,new=new)