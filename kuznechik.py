from math import ceil
x, y, d, a, b = list(map(int, input().split())); res = float('inf'); res_changed = False
if a > b:
    a, b = b, a
if x <= a and y <= a:
    if abs(x - y) % d == 0:
        res = min(res, abs(x - y) // d); res_changed = True
    if abs(a - y) % d == 0:
        res = min(res, ceil(abs(a - x) / d) + abs(a - y) // d); res_changed = True
    print(res if res_changed else -1)
elif a <= x <= b and a <= y <= b:
    if abs(x - y) % d == 0:
        res = min(res, abs(x - y) // d); res_changed = True
    if abs(a - y) % d == 0:
        res = min(res, ceil(abs(a - x) / d) + abs(a - y) // d); res_changed = True
    if abs(b - y) % d == 0:
        res = min(res, ceil(abs(b - x) / d) + abs(b - y) // d); res_changed = True
    print(res if res_changed else -1)
elif x >= b and y >= b:
    if abs(x - y) % d == 0:
        res = min(res, abs(x - y) // d); res_changed = True
    if abs(b - y) % d == 0:
        res = min(res, ceil(abs(b - x) / d) + abs(b - y) // d); res_changed = True
    print(res if res_changed else -1)
else:
    print(-1)