newxlist = []
tlist = []
xlist = []
N = int(input())
t = [0] * N
x = [0] * N
for i in range(N):
    #t[i], x[i] = mylist.append(input().split())
    #mydict=dict(mylist)
    tlist.append(t[i])
    xlist.append(x[i])
newxlist=sorted(xlist)
dict_from_list = dict(zip(tlist, newxlist))
print(dict_from_list)