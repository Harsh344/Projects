import serial
import time
import pyautogui
x=5
def control():
    AS=serial.Serial('COM3',9600)
    time.sleep(1)
    
    while True:
        incoming= str (AS.readline())
        print (incoming)
    
        if 'Vup' in incoming:
            pyautogui.press('right')
    
    if 'Vdn' in incoming:
        pyautogui.press('left')
