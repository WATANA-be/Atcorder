list = []
a,b,c = map(int,input().split())
for i in range(a):
    d,e = map(int,input().split())
    list.append(e/d)
    think = max(list)#考える点
    h = think/d
    d1 = think/h

s = (c-h)/(b-d1)
t = c - s*b

print(t)