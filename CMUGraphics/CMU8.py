"""For more complex objects it is quite tedious to have to write them first and then change each element as required.
It is easier to write the code where it is needed the first time.
However, I need some Variables (or, to put it more clearly, the objects) to be global - they are created in one 
Function and have to be recognized in another Function.
"""

from cmu_graphics import *


def onMousePress(mouseX, mouseY):

    #Global Variable - I need to address it in the next function 
    global doubleKreis 
    
    Kreis1 = Circle(mouseX, mouseY, 20, fill='red')
    Kreis2 = Circle(mouseX+20, mouseY, 20, fill='blue')

    doubleKreis = Group(Kreis1, Kreis2)
    doubleKreis.visible = True

def onMouseRelease(mouseX, mouseY):    
    global doubleKreis
    doubleKreis.visible = False
    

cmu_graphics.run()