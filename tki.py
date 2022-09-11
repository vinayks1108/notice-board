try:
    from pynput.keyboard import Key, Controller
except:
    os.system('pip install pynput')
    from pynput.keyboard import Key, Controller   
from time import sleep
import os
os.system("trial2.html")
sleep(4)
keyboard = Controller()
keyboard.press(Key.f11)
sleep(1)
keyboard.release(Key.f11)
