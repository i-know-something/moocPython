
def judge(i):
    st=str(i)
    a=eval(st[0])
    b=eval(st[1])
    c=eval(st[2])
    if pow(a,3)+pow(b,3)+pow(c,3)==i:
        print(1)
    else:
        print(2)




flag_begin=0;

for i in range(100,1000):
    if judge(i)==1:
        if(flag_begin==1):
            print(",")
        else:
            flag_begin=1
        print(i)

