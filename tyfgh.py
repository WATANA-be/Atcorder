x,y,z = map(int, input().split())
try:
    wari2=y/x
except ZeroDivisionError:
    wari2=y
try:
    a=(((wari2*int(z)-1)))
except ZeroDivisionError:
    a=y*int(x)*int(z)-1
try:
    wari=y//x
except ZeroDivisionError:
    wari=y

try:
    if (wari2)-(wari)!=0:
        b=a//1
        c=b+1
        print(int(c))
    elif ((((wari2)*z)-1))<0:
        print('0')
    else:
        print((int((wari2)*z)-1))
except ZeroDivisionError:
    wari=y
    if (wari2)-(wari)!=0:
        b=a//1
        c=b+1
        print(int(c))
    elif ((((wari2)*z)-1))<0:
        print('0')
    else:
        print((int((wari2)*z)-1))
