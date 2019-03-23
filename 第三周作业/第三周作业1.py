# 五星之位置与画法如下：

# (1) 为便于确定五星之位置，先将旗面对分为四个相等的长方形，将左上方之长方形上下划为十等分，左右划为十五等分。

# (2) 大五角星的中心点，在该长方形上五下五、左五右十 (-10,5) 之处。其画法为：以此点为圆心，以三等分为半径作一圆。
#     在此圆周上，定出五个等距离的点，其一点须位于圆之正上方。然后将此五点中各相隔的两点相联，使各成一直线。
#     此五直线所构成之外轮廓线，即为所需之大五角星。五角星之一个角尖正向
# (3) 四颗小五角星的中心点，第一点在该长方形上二下八、左十右五 (-5,8) 之处，第二点在上四下六、左十二右三 (-3,6) 之处，
#     第三点在上七下三、左十二右三 (-3,3) 之处，第四点在上九下一、左十右五 (-5,1) 之处。其画法为：以以上四点为圆心，
#     各以一等分为半径，分别作四个圆。

#     在每个圆上各定出五个等距离的点，其中均须各有一点位于大五角星中心点与以上四个圆心的各联结线上。
#     然后用构成大五角星的同样方法，构成小五角星。此四颗小五角星均各有一个角尖正对大五角星的中心点。


import turtle as t
import numpy as np

def draw_star(head,size,x,y):  #head为顶角指向 size为外接圆半径 (x,y)为外接圆圆心
    length=size*np.cos(np.deg2rad(18))-size*np.sin(np.deg2rad(18))*np.tan(np.deg2rad(36))
    t.goto(x,y)
    t.setheading(90)
    t.left(head-18)
    t.forward(size)
    t.right(162)
    t.fillcolor('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(length)
        t.left(72)
        t.forward(length)
        t.right(144)
    t.end_fill()

def draw_flag(size,x=0,y=0):   #size为每等分小格的边长   (x,y)为旗子中心坐标
    t.setheading(0)
    t.fillcolor('red')
    length=30*size
    width=20*size
    t.goto(x-0.5*length,y+0.5*width)
    t.begin_fill()
    for i in range(2):
        t.forward(length)
        t.right(90)
        t.forward(width)
        t.right(90)
    t.end_fill()

def draw_national_flag(grid_size):
    t.penup()
    t.hideturtle()
    t.speed(0)
    draw_flag(grid_size)  
    draw_star(90,3*grid_size,-10*grid_size,5*grid_size)    #大五角星
    x0,y0=-10,5                                       #小五角星
    for (x,y) in [(-5,1),(-3,3),(-3,6),(-5,8)]:
        heading=180+np.degrees(np.arctan((y-y0)/(x-x0)))   #调整小五角星顶角指向大五角星中心
        draw_star(heading,grid_size,x*grid_size,y*grid_size)
    t.exitonclick()

draw_national_flag(25)
