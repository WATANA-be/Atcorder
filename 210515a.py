a,b,c= map(int, input().split())
mylist = [a,b,c]
newlist = sorted(mylist)

if newlist[2]-newlist[1] == newlist[1]-newlist[0]:
    print("Yes")
else:
    print("No")