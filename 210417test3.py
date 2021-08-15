x,y,z = map(int, input().split())
a=(((int(y)/int(x)*int(z)-1)))
try:
    wari=y//x
    if (y/x)-(wari)!=0:
        b=a//1
        c=b+1
        print(int(c))
    else:
        print((int((y/x)*z)-1))
except ZeroDivisionError(a):
    print('0')