# 请在...补充一行或多行代码

import turtle as t
def koch(size, n):
    ...
    if n==0:
        t.fd(size)
    else:
        for angle in [0,60,-120,60]:
            t.left(angle)
            koch(size/3,n-1)



def main(n):
    t.tracer(0)
    t.speed(0)
    t.setup(600,600)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.pensize(1)

    for i in range(3):
        koch(400,n)
        t.right(120)
    t.update()
    t.done()
try:
    n = eval(input("请输入科赫曲线的阶: "))
    main(n)
except:
    print("输入错误")