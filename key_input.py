"""Hooking key"""

import sys
import tty
import termios

class KeyboardHandle:       
    def __call__(self):
        fileno = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fileno)
        try:
            tty.setraw(sys.stdin.fileno())
            char = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fileno, termios.TCSADRAIN, old_settings)
        return char

def getOneKeycode():
    inkey = KeyboardHandle()
    while 1:
        char = inkey()
        if char != '':
            break
    return char

def getArrowKeyCode():
    while 1:
        char = getOneKeycode()

        if ord(char) == 27:
            char = getOneKeycode()
            if ord(char) == 91:
                return ord(getOneKeycode())

def main():
    for i in range(0, 5):
        keycode = getArrowKeyCode()
        print ("Arrow=>" + str(keycode))


if __name__=='__main__':
    main()

