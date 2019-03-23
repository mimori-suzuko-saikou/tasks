import turtle as t

def leaf(length,width):       #绘制树叶
    t.color('green')
    t.begin_fill()
    t.left(10)
    t.right(width)
    t.circle(length,2*width)
    t.left(180-2*width)
    t.circle(length,2*width)
    t.left(180-width)
    t.end_fill()
    t.right(10)
    t.color('saddlebrown')


def branch(length,pensize):           #绘制树枝
    t.pensize(pensize)
    t.color('saddlebrown')
    if length > 60:
        t.forward(length) 
        t.right(angle_r)  
        branch(0.7*length,pensize-2)    #递归绘制小树枝
        t.left(angle_r+angle_l)  
        branch(0.7*length,pensize-2) 
        t.right(angle_l) 
        t.backward(length)  
    else:
        leaf(60,75)

t.penup()
t.setheading(90)  
t.sety(-300) 
t.pendown()
t.speed(0)
angle_r=40
angle_l=20
branch(200,10)
t.exitonclick()
