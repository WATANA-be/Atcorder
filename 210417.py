n,m = map(int, input().split())
def gcd(n, m):
    if n > m:
        m,n=n,m
    i = 1
    while i <= n:
        if n % i == 0 and m % i == 0:
            gcd = i
        i = i + 1
    return gcd
print(gcd(n,m))