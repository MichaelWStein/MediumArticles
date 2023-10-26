""" I can access the whole group as well as the elmeents in a Group, as long as I have named them 
(created objects).
"""

from cmu_graphics import *

centerX = 200
centerY = 200

Kreis1 = Circle(centerX, centerY, 40, fill='red')
Kreis2 = Circle(centerX+40, centerY, 40, fill='blue')

DoubleKreis = Group(
    Kreis1, Kreis2
) 

def onMousePress(mouseX, mouseY):
    Kreis1.fill = 'blue'
    Kreis2.fill = 'red'

def onMouseRelease(mouseX, mouseY):
    DoubleKreis.fill = 'red'

cmu_graphics.run()