"""Hooking key"""

import sys
import tty
import termios
import os

# CURSOR_UP =  u"\u001b[" + str(1) + "A"
# printCurosrUp = lambda n: u"\u001b[" + str(n) + "A"
def printCurosrUp2(n):
    sys.stdout.write (u"\u001b[" + str(n) + "A")

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
    clHeight, clWidth = os.popen('stty size').read().split()
    clWidth = int(clWidth)

    fileLines = []
    for line in open('test.txt'):
        fileLines.append(line.strip())

    offsetY = 0
    offsetX = 0
    for i in range(0, 5):
        print ("clHeight=" + clHeight + " clWidth=" + str(clWidth))

        for j in range(offsetY, int(clHeight) - 2 + offsetY):
            printLine = fileLines[j][offsetX:clWidth - offsetX]
            printLine = printLine.replace("\t", " ")
            sys.stdout.write (printLine)

            # print ("")
            print("".rjust(clWidth - len(printLine), ' '))

        keycode = getArrowKeyCode()
        if keycode == 65 and offsetY > 0:
            offsetY -= 1

        if keycode == 66 and offsetY < len(fileLines):
            offsetY += 1

        if keycode == 67:
            offsetX += 1

        if keycode == 68 and offsetX > 0:
            offsetX -= 1

        printCurosrUp2(int(clHeight) - 1)


if __name__=='__main__':
    main()

