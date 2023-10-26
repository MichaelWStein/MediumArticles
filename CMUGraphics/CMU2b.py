""" The second object overwrites the first one

"""

from cmu_graphics import *

Kreis = Circle(200, 200, 80, fill = 'blue')
Kreis = Rect(10, 10, 30, 40, fill = 'blue')

def onMousePress(mouseX, mouseY):
    Kreis.fill = 'blue'

def onMouseRelease(mouseX, mouseY):
    Kreis.fill = 'red'

cmu_graphics.run()