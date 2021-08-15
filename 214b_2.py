x,y = map(int,input().split())
a=0
b=0
c=0
kei=0
if x>=y:
    t=x
else:
    t=y
for i in range(t):
    if a+b+c<=x and a*b*c<=y:
        kei+=1
        a+=1
    for j in range(t):
        if a+b+c<=x and a*b*c<=y:
            kei+=1
            b+=1
        for k in range(t):
            if a+b+c<=x and a*b*c<=y:
                kei+=1
                c+=1
            
if a!=b!=c:               
    kei2=kei*6
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and b!=c):
    kei2=kei*3
else:
    kei2=kei


print(kei2)