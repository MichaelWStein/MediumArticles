"""The goal is to create double circles at the location of the mouse click. First I try with a function.
This works for creating circles at the location of the mouse.
"""

from cmu_graphics import *

def doubleKreis(x_pos, y_pos):
    Kreis1 = Circle(x_pos, y_pos, 20, fill='red')
    Kreis2 = Circle(x_pos+20, y_pos, 20, fill='blue')


def onMousePress(mouseX, mouseY):
    doubleKreis(mouseX, mouseY)


cmu_graphics.run()