#本函数无法自动停止绘制！！！
#显示当前时间，精确度0.1s

import turtle as t
import time

Reg = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,\
    0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0xff]

def DrawLine(x,y,degree):
    t.up()
    t.goto(x,y)
    t.pencolor("black")
    t.pensize(10)
    t.seth(degree)
    t.down()
                #Line:  _______
                #      <_______>
    t.left(45)         
    t.fd(10)           
    t.right(45)                
    t.fd(80)                
    t.right(45)
    t.fd(10)
    t.right(90)
    t.fd(10)
    t.right(45)
    t.fd(80)
    t.right(45)
    t.fd(10)

def DrawDigital(n,x,y):
    
    t.speed(0)
    if 0x01 & Reg[n]:DrawLine(x+10,y,0)
    if 0x02 & Reg[n]:DrawLine(x+110,y,-90)
    if 0x04 & Reg[n]:DrawLine(x+110,y-110,-90)
    if 0x08 & Reg[n]:DrawLine(x+10,y-200,0)
    if 0x10 & Reg[n]:DrawLine(x+10,y-110,-90)
    if 0x20 & Reg[n]:DrawLine(x+10,y,-90)
    if 0x40 & Reg[n]:DrawLine(x+10,y-100,0)
    if 0x80 & Reg[n]:t.up();t.goto(x+150,y-220);t.circle(5)

def DrawColon(x,y):
    t.up();t.goto(x,y-50);t.down()
    t.circle(5)
    t.up();t.goto(x,y-150);t.down()
    t.circle(5)

if __name__=="__main__":

    sec=0
    s=''
    t.setup(1200,300)
    
    while 1:
        time.sleep(0.1)
        TN=time.localtime()

        if sec!=TN[5]:
            sec=TN[5]

            s="{:02d}{:02d}{:02d}".format(TN[3],TN[4],TN[5])

            x=-550
            y=120
            
            t.clear()
            t.tracer(0)
            for i in range(6):
                if i%2==0 and i!=0:
                    DrawColon(x+i*150+25,y)
                    x+=50
                DrawDigital(eval(s[i]),x+i*150,y)
            t.update()
    
    t.done()