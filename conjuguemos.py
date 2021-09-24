from pynput.keyboard import Key, Listener
from pynput.mouse import Button, Controller
import time

"""
Conjuguemos
Author: Josh Richardson
Description:
this is to help with typing accented letters on 
https://conjuguemos.com/ graded practice section

console help
cd accentedletters
python conjuguemos.py
"""
#setting simple name for mouse controller
mouse = Controller()


def on_press(key):
    print(key)
    #when left shift is pressed
    if key == Key.shift_l:
        #for accented a, e, i, o, n
        mouse.position = (1192, 504)
        mouse.press(Button.left)
        time.sleep(0.002)
        mouse.release(Button.left)
    #when left control is pressed
    elif key == Key.ctrl_l:
        #for accented u
        mouse.position = (1144, 504)
        mouse.press(Button.left)
        time.sleep(0.002)
        mouse.release(Button.left)

#on release of esc end with "user ended"
def on_release(key):
    if key == Key.esc:
        print("user ended")
        return False
    print('release')
    return True

#calling listener for shift and ctrl
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
