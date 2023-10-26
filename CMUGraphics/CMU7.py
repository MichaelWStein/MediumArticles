"""The goal is now to create the two circles only when I press the mouse, they are invisible as soon as I relelase the mouse.
The first solution is to create two objects, then to manipulate them on mouseclick. 
"""

from cmu_graphics import *
x_pos = 40
y_pos = 40

Kreis1 = Circle(x_pos, y_pos, 20, fill='red')
Kreis2 = Circle(x_pos+20, y_pos, 20, fill='blue')

doubleKreis = Group(Kreis1, Kreis2)
doubleKreis.visible = False


def onMousePress(mouseX, mouseY):
    Kreis1.centerX = mouseX
    Kreis1.centerY = mouseY
    Kreis2.centerX = mouseX+20 
    Kreis2.centerY = mouseY
    doubleKreis.visible = True

def onMouseRelease(mouseX, mouseY):    
    doubleKreis.visible = False
    

cmu_graphics.run()