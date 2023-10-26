#import * is not recommended, but as we are only importing one module
#and all cmu-graphics example are using it, I'll stick with it.
#Better is import cmu_graphics as cmu and then use cmu.Circle... 

from cmu_graphics import *

#simple program to draw a circle

Circle(200, 200, 80, fill = 'blue')

cmu_graphics.run()