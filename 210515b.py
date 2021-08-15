tlist=[]
xlist=[]
N = int(input())
t = [0] * N
x = [0] * N
for i in range(N):
    t[i], x[i] = input().split()
    tlist.append(t[i])
    xlist.append(x[i])
newtlist=sorted(tlist)
newxlist=sorted(xlist)

print()
