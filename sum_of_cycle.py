alpha = input(); s = sum(map(int, list(alpha))); n = len(alpha)
base_sum = s; res = 0
for _ in range(n - 1):
    res += s % 10
    s = base_sum + s // 10
res += sum(map(int, list(str(s))))
print(res)