"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Carla Archuleta.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
import rosegraphics as rg
window = rg.TurtleWindow()
dean = rg.SimpleTurtle()
kate = rg.SimpleTurtle()
dean.pen = rg.Pen('purple',5)
kate.pen = rg.Pen('blue',10)
dean.speed = 10
kate.speed = 50
size = 100
for k in range(5):
    dean.draw_circle(size)
    dean.pen_up()
    dean.forward(50)
    dean.right(50)
    dean.pen_down()
    size = size - 15
kate.left(100)
size1 = 100
for k in range(30):
    kate.draw_regular_polygon(8,size1)
    kate.pen_up()
    kate.backward(100)
    kate.left(100)
    kate.pen_down()
    size1 = size1 - 2
window.close_on_mouse_click()

#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
