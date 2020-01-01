import pyautogui as p
import time as t       
import pyscreenshot as ImageGrab
from numpy import *
from PIL import ImageOps


replaybutton=(990,425)         
dinosaur=(736,426)

def restart():
    p.click(replaybutton)

def pressSpace():
    p.keyDown('space')
    t.sleep(0.05)
    print("Jump!")
    p.keyUp('space')

def imagegrab():
    box=(dinosaur[0]+72,dinosaur[1],dinosaur[0]+87,dinosaur[1]+44)
    image=ImageGrab.grab(box)
    grayimage=ImageOps.grayscale(image)
    a=array(grayimage.getcolors())
    return(a[0][0])

def main():
    restart()
    while True:
        if imagegrab()>80:
            pressSpace()
            t.sleep(0.05)

t.sleep(2)
pressSpace()
main()
     