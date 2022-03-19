fun = lambda x : -3*x**2 + 5*x + 9
l, r = -5, 5; l1, r1 = l + (1/3) * (r - l), r - (1/3) * (r - l)
while r - l >= 10**(-3):
    if fun(l1) < fun(r1):
        l = l1; l1, r1 = l + (1/3) * (r - l), r - (1/3) * (r - l)
    elif fun(l1) > fun(r1):
        r = r1; l1, r1 = l + (1/3) * (r - l), r - (1/3) * (r - l)
print((l + r) / 2)