from turtle import *
from math import *
def Rectangle():
    color('red','red')
    speed(10)
    penup()
    goto(-500,-300)
    pendown()
    begin_fill()
    for i in range(2):
        forward(960)
        left(90)
        forward(640)
        left(90)
    end_fill()
def draw_star(radius,star_x,star_y):
    color('yellow','yellow')
    speed(10)
    goto(star_x,star_y)
    pt=[]
    pt.append(pos())
    i=0
    while(i<4):
        circle(radius,72)
        pt.append(pos())
        i+=1
    circle(radius,72)
    begin_fill()
    goto(pt[0])
    pendown()
    for i in [3,1,4,2,0]:
        goto(pt[i])
    end_fill()
def found_small_star(angle,star_center):
    #此函数的作用是找到副星的起始位置
    penup()
    setheading(0)
    goto(-340,180)
    left(angle)
    goto(star_center)
    backward(32)
    right(90)
    draw_star(32,xcor(),ycor())
def found_big_star():
    #此函数的作用是找到主星的起始位置
    penup()
    setheading(0)
    goto(-340,180)
    left(90)
    forward(32*3)
    left(90)
    draw_star(96,xcor(),ycor())
def main():
    Rectangle()
    found_big_star()
    found_small_star(atan(3/5)*180/pi,(-180,276))
    found_small_star(atan(1/7)*180/pi,(-116,212))
    found_small_star(-atan(2/7)*180/pi,(-116,116))
    found_small_star(-atan(4/5)*180/pi,(-180,52))
    hideturtle()
if __name__ == '__main__':
    main()
