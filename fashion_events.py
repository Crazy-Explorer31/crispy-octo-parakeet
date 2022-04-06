def main():
    n, m = list(map(int, input().split()))
    costs = {}; res = [0] * n; ans = 0
    for _ in range(m):
        l, r, x = list(map(int, input().split())); l -= 1
        if (l, r) in costs.keys() and x > costs[(l, r)]:
            costs[(l, r)] = x
        elif (l, r) not in costs.keys():
            costs[(l, r)] = x
    costs = {u : v for u, v in sorted(costs.items(), key = lambda x : x[1])}
    for (l, r), x in costs.items():
        delta = 0
        for i in range(l, r):
            delta += x - res[i]; res[i] = x
        ans += delta
    print(ans)
main()