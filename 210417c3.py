n,m = map(int, input().split())
def euclid(n, m):
    if n < m:
        n, m = m, n
    while m != 0:
        n, m = m, n % m # 「%」は割った余り
    return n
print(euclid(n,m))