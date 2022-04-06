from math import ceil
def fucking(n):
    res1, res2 = 0, 0
    while not(n & 1):
        res1 += 1; n >>= 1
    while n % 3 == 0:
        res2 += 1; n //= 3
    if n != 1:
        return None
    else:
        return res1, res2
n, k = list(map(int, input().split()))
fuck = fucking(n)
if fuck is None:
    print(0)
else:
    alpha, beta = fuck
    if ceil(alpha / 2) + beta > k:
        print(0)
    else:
        if k - beta >= alpha:
            print((alpha // 2 + 1) % (10 ** 9 + 7))
        else:
            print(((alpha - 2 * (alpha - k + beta)) // 2 + 1) % (10 ** 9 + 7))