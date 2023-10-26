""" Now changing the colour of the circle on mouse click

"""

from cmu_graphics import *

Kreis = Circle(200, 200, 80, fill = 'blue')

def onMousePress(mouseX, mouseY):
    Kreis.fill = 'blue'

def onMouseRelease(mouseX, mouseY):
    Kreis.fill = 'red'

cmu_graphics.run()