from pynput.keyboard import Key, Listener, Controller
import time
kb = Controller()


def paste():
    kb.press(Key.ctrl)
    time.sleep(0.2)
    kb.press('v')
    time.sleep(0.2)
    kb.release(Key.ctrl)
    time.sleep(0.2)
    kb.release('v')
    time.sleep(0.002)
    kb.press(Key.enter)


def on_release(key):
    if key == Key.esc:
        return False


with Listener(on_release=on_release) as listener:
    listener.join()


while True:
    paste()
