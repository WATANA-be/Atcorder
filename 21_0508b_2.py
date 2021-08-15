#N,K = map(int, input().split())
N=int(2021)
K=int(4)
c=0
for i in range(K):
    if int(N)%200==0:
        N=(int(N)/200)
    #elif int(N)%200!=0:
    else:
        N=(str(N)+str(200))

print(int(N))
