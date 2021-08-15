import math
N = int(input())

x = [0] * N
y = [0] * N
for i in range(N):
    x[i], y[i] = map(int, input().split())
ans = 0
list = []
for i in range(N):
    for j in range(N):
        if math.sqrt(pow(x[i]-x[j],2) + pow(y[i] - y[j],2)) > ans:
            list.append(math.sqrt(pow(x[i]-x[j],2) + pow(y[i] - y[j],2)))

#nums_unique = list(set(list))
#list.sort(list, reverse=True)
#print(list[1])
print(list)