neighbors = lambda i, j, n, m : [z for z in {(i - 2, j + 1), (i - 2, j - 1), (i - 1, j - 2), (i + 1, j - 2)}
                                 if 0 <= z[0] < n and 0 <= z[1] < m]
n, m = list(map(int, input().split())); dynamic = [[0] * m for _ in range(n)]; dynamic[0][0] = 1
for kj in range(1, m):
    i = 0
    for j in range(kj, -1, -1):
        if i == n:
            break
        s = sum([dynamic[p][q] for p, q in neighbors(i, j, n, m)])
        if s >= 10**9 + 123:
            s = s % (10**9 + 123)
        dynamic[i][j] += s
        i += 1
for ki in range(1, n):
    j = m - 1
    for i in range(ki, n):
        if j < 0:
            break
        s = sum([dynamic[p][q] for p, q in neighbors(i, j, n, m)])
        if s >= 10**9 + 123:
            s = s % (10**9 + 123)
        dynamic[i][j] += s
        j -= 1
print(dynamic[n - 1][m - 1])
