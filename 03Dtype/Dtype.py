#daydayup3.py



dayup=1.0
dayfactor =0.01
result_everyday=pow(1.01,365)

def calc():
    result=dayup
    for i in range(365):
        result=result*(1-0.01) if i%7==6 or i%7==0 else result*(1+dayfactor)
    return result

while calc()<result_everyday :
    dayfactor+=0.001

print("daydayup{:.3f},the result can be same as everydayup: {:.3f}".format(dayfactor,calc()))
