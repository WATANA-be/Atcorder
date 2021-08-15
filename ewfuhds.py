x,y,z = map(int, input().split())
try:
    wari2=y/x
except ZeroDivisionError:
    wari2=0
try:
    a=(((int(y)/int(x)*int(z)-1)))
except ZeroDivisionError:
    a=0
try:
    wari=y//x
except ZeroDivisionError:
    wari=0
try:
    if (y/x)-(wari)!=0:
        b=a//1
        c=b+1
        print(int(c))
    elif ((((y/x)*z)-1))<0:
        print('0')
    else:
        print((int((y/x)*z)-1))
except ZeroDivisionError:
    print("0")