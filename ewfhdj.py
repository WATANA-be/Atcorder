x,y,z = map(int, input().split())
a=(((int(y)/int(x)*int(z)-1)))
if int(y)/int(x).is_integer()==False:
    b=a//1
    c=b+1
    print(int(c))
else:
    print(((y/x)*z)-1)