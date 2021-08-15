from functools import reduce
n1 = int(input())

l = [int(x) for x in list(str(n))]
#020384
for i in range(len(l)):
    if l[i]=="6":#" "でくくってなかった
        l[i]=9
    elif l[i]=="9":
        l[i]=6
#new_n = int(reduce(lambda x, y: x + y, [str(x) for x in l]))
#print(new_n)
#n2 = reduce( lambda a,b:10*a+b, list)
#print(n2)
if l[i]!=0:
    new_n = int(reduce(lambda x, y: x + y, [str(x) for x in l]))
    print(new_n)
else:
    new_n = int(reduce(lambda x, y: x + y, [str(x) for x in l]))
    print("0"+str(new_n))
