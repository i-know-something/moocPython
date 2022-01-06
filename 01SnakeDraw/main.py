import DrawDef
#一次性程序，turtle.done之后无法再次调用，懒得关心turtle了凑活着用吧
key=input("请输入绘制的图形：\n1.蛇形  2.正方形  3.六边形    4.叠边形   5.风轮")

if key in ['1','2','3','4','5']:
    if key=='1':
        DrawDef.DrawSnake()
    elif key=='2':
        DrawDef.DrawRect()
    elif key=='3':
        DrawDef.DrawHexagon()
    elif key=='4':
        DrawDef.Draw100()
    elif key=='5':
        DrawDef.DrawWindmill()
else:
    print("what are you saying???")
 #   key=input("请输入绘制的图形：\n1.蛇形 2.rect  3.Hexagon ")

