from turtle import *

def square(x,y,size,color_name):
    up()
    goto(x,y)
    down()
    color(color_name)
    begin_fill()
    for i in range(4):
        forward(size)
        left(90)
    end_fill()
def line(x1,y1,x2,y2,line_width=1,color_name="black"):
    up()
    goto(x1,y1)
    down()
    width(line_width)
    color(color_name)
    goto(x2,y2)
