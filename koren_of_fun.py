def polinom(array, x):
    res = 0
    for n in range(len(array)):
        res += x**(len(array) - n - 1) * array[n]
    return res
x0, y0, r = list(map(int, input().split()))
degree = int(input())
coefs = list(map(int, input().split()))
super_x = int(input())
left, right = super_x, x0 + r; res = (left + right) / 2; value = polinom(coefs, res)
while abs(((res - x0)**2 + (value - y0)**2) ** 0.5 - r) >= 10**(-7):
    if ((res - x0)**2 + (value - y0)**2)**0.5 > r:
        right = res; res = (left + right) / 2; value = polinom(coefs, res)
    elif ((res - x0)**2 + (value - y0)**2)**0.5 < r:
        left = res; res = (left + right) / 2; value = polinom(coefs, res)
print(res)