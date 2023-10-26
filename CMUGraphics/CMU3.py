""" Creating a double circle. Obviously I could create each circle separately (let's say Kreis1 = ... and Kreis2 = ...), but this
is rather awkward for more complex objects I want to manipulate, so I use the Croup collection. However, only the group can be
changed.

"""

from cmu_graphics import *

centerX = 200
centerY = 200

DoubleKreis = Group(
    Circle(centerX, centerY, 40, fill='red'),
    Circle(centerX+40, centerY, 40, fill='blue')
) 

def onMousePress(mouseX, mouseY):
    DoubleKreis.fill = 'blue'

def onMouseRelease(mouseX, mouseY):
    DoubleKreis.fill = 'red'

cmu_graphics.run()