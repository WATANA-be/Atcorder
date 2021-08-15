x,y = map(int,input().split())
kei=0
a,b,c=0,0,0
def add():
    global a,b,c
    for i in range(10000):
        a+=1
        for j in range(10000):
            b+=1
            for k in range(10000):
                c+=1
for m in range(10000):
    add()
    if a+b+c<=x and a*b*c<=y:
        kei+=1
print(kei)
