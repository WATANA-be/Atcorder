N,K = map(int, input().split())

for i in range(K):
    if N%200==0:
        ans=(N/200)
    elif N%200!=0:
        ans=((N*100)+(200))

print(ans)