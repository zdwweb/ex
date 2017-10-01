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
    goto(star_x,star_y)
    pt=[]
    pt.append(pos())
    i=0
    while(i<4):
        circle(radius,72)
        pt.append(pos())
        i+=1
    speed(6)
    begin_fill()
    goto(pt[0])
    pendown()
    for i in [3,1,4,2,0]:
        goto(pt[i])
    end_fill()
Rectangle()
#主星
penup()
setheading(0)
goto(-340,180)
left(90)
forward(32*3)
left(90)
draw_star(96,xcor(),ycor())
#星一
penup()
setheading(0)
goto(-340,180)
left(atan(3/5)*180//pi)
goto(-180,276)#小星中心
backward(32)
right(90)
draw_star(32,xcor(),ycor())
#星二
penup()
setheading(0)
goto(-340,180)
left(atan(1/7)*180//pi)
goto(-116,212)
backward(32)
right(90)
draw_star(32,xcor(),ycor())
#星三
penup()
setheading(0)
goto(-340,180)
right(atan(2/7)*180//pi)
goto(-116,116)
backward(32)
right(90)
draw_star(32,xcor(),ycor())
#星四
penup()
setheading(0)
goto(-340,180)
right(atan(4/5)*180//pi)
goto(-180,52)
backward(32)
right(90)
draw_star(32,xcor(),ycor())
hideturtle()

