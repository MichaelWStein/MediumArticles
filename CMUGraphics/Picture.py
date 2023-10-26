from cmu_graphics import *

# put your code here

#Sky
Rect(0, 0, 500, 400, fill=gradient(rgb(255, 255, 153), rgb(255, 102, 0), rgb(255, 0, 0),  start='top-left'))

#Sun
Star(40, 40, 50, 8, fill=rgb(255, 165, 0))
Circle(40, 40, 30, fill=rgb(255, 255, 153))

#Water
Rect(0, 200, 400, 200, fill=gradient(rgb(51, 153, 255), rgb(204, 255, 255), start='top'))

#Sand
Rect(0, 300, 400, 200, fill=gradient(rgb(255, 255, 153), rgb(255, 215, 0), start='top'))

#Sailboat, made invisible if space=bar pressed
s_boat = Polygon(300, 200, 330, 120, 360, 200, fill="ivory")
#Visibility
def onKeyPress(key):
    if (key == 'space'):
        s_boat.visible = not s_boat.visible

#Rocks on the Beach
    #big rock
Polygon(0, 400, 0, 300, 40, 250, 60, 320, 100, 400, fill="dimGray")
    #small rocks
    #set parameter for first rock and draw rock
x11 = 150
x12 = 390
x21 = 160
x22 = 370
x31 = 165
x32 = 380
x41 = 170
x42 = 385

Polygon(x11, x12, x21, x22, x31, x32, x41, x42, fill="dimGray")

    #next rock - moved to the right and higher
right = 30
height = -20
x11 = x11 + right
x12 = x12 + height
x21 = x21 + right
x22 = x22 + height
x31 = x31 + right
x32 = x32 + height
x41 = x41 + right
x42 = x42 + height

Polygon(x11, x12, x21, x22, x31, x32, x41, x42, fill="dimGray")

    #next rock
right = 100
height = 20
x11 = x11 + right
x12 = x12 + height
x21 = x21 + right
x22 = x22 + height
x31 = x31 + right
x32 = x32 + height
x41 = x41 + right
x42 = x42 + height

Polygon(x11, x12, x21, x22, x31, x32, x41, x42, fill="dimGray")

cmu_graphics.run()