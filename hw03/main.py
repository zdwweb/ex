from turtle import *
from math import *
origin_x,origin_y=-500,-300 #自定义原点
def Rectangle(length,width):
    color('red','red')
    speed(10)
    penup()
    goto(origin_x,origin_y)
    pendown()
    begin_fill()
    for i in range(2):
        forward(length)
        left(90)
        forward(width)
        left(90)
    end_fill()
def draw_star(radius,star_x,star_y):
    #以五等分圆法绘制五角星
    color('yellow','yellow')
    speed(10)
    goto(star_x,star_y)
    pt=[]
    pt.append(pos())
    for i in range(4):
        circle(radius,72)
        pt.append(pos())
    circle(radius,72)
    begin_fill()
    goto(pt[0])
    pendown()
    for i in [3,1,4,2,0]:
        goto(pt[i])
    end_fill()
def found_star(angle,radius,star_center=None):
    #定位起始位置并画出五角星
    penup()
    setheading(0)
    goto(big_star_center)
    if(angle==90):
        left(90)
        forward(radius)
        left(90)
        draw_star(radius,xcor(),ycor())
    else:
        left(angle)
        goto(star_center)
        backward(radius)
        right(90)
        draw_star(radius,xcor(),ycor())
def main():
    length,width=960,640
    small_radius=32
    big_radius=small_radius*3
    unit=width/20 
    base_x,base_y=origin_x,origin_y+unit*10 #以此基点定位五角星的外接圆心
    global big_star_center
    big_star_center=(base_x+unit*5,base_y+unit*5)
    Rectangle(length,width)
    found_star(90,big_radius)
    found_star(atan(3/5)*180/pi,small_radius,(base_x+unit*10,base_y+unit*8))
    found_star(atan(1/7)*180/pi,small_radius,(base_x+unit*12,base_y+unit*6))
    found_star(-atan(2/7)*180/pi,small_radius,(base_x+unit*12,base_y+unit*3))
    found_star(-atan(4/5)*180/pi,small_radius,(base_x+unit*10,base_y+unit*1))
    hideturtle()
if __name__ == '__main__':
    main()
