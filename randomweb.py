from pynput.keyboard import Key, Listener, Controller
import random

kb = Controller()
ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def on_press(key):
    print(key)
    if key == Key.shift_l:
        kb.release(Key.shift_l)
        kb.type('https:')
        kb.tap('/')
        kb.tap('/')
        kb.type('prnt.sc')
        kb.tap('/')
        char2()
        number4()
        kb.tap(Key.enter)


def char2():
    for i in range(2):
        kb.type(ab[random.randrange(25)])


def number4():
    for i in range(4):
        kb.type(str(random.randrange(10)))


def on_release(key):
    if key == Key.esc:
        print("user ended")
        return False
    print('release')
    return True


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
