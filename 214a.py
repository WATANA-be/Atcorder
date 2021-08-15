n=int(input())
kei=0
if n>=125:
    kei=4*n
elif 125<=n<=211:
    kei=4*125+6*(n-125)
elif 212<=n<=214:
    kei=4*125+6*86+8*(n-125-86)
print(kei)
