import turtle as t

#Draw Snake

def DrawSnake():
    t.setup(650,350,200,200)
    t.penup()
    t.fd(-250)
    t.pendown()
    t.pensize(15)
    t.pencolor("purple")
    t.seth(-40)
    for i in range(4):
        t.circle(40,80)
        t.circle(-40,80)
    t.circle(40,80/2)
    t.fd(40)
    t.circle(16,180)
    t.fd(40*2/3)
    t.done()

#draw rect
def DrawRect():
    t.setup(400,400,0,0)
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    t.pensize(10)
    t.pencolor(0.5,0.5,0.5)

    for i in range(4):
        t.fd(200)
        t.left(90)

    t.done()

#draw hexagon
def DrawHexagon():
    t.setup(400,400,0,0)
    t.penup()
    t.goto(-100,0)
    t.pendown()
    t.pensize(10)
    t.pencolor(0.5,0.5,0.5)
    t.left(60)

    for i in range(6):
        t.fd(100)
        t.right(60)

    t.done()

def Draw100():
    t.setup(400,400,0,0)
    t.pensize(10)
    t.pencolor(0.5,0.5,0.5)
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    for i in range (9):
        t.fd(100)
        t.left(80)
    t.done()

def DrawWindmill():
    t.setup(400,400,0,0)
    t.pensize(10)
    t.pencolor(0.5,0.5,0.5)

    for i in range(4):
        t.fd(100)
        t.left(90)
        t.circle(100,45)
        t.home()
        t.left(90*(i+1))

    t.done()