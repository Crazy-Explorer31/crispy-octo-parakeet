def count_attacked(node, graph, attacked):
    res = 0
    for n in graph[node]:
        if attacked[n]:
            res += 1
    return res
comps, nets = list(map(int, input().split())); min_attacked = list(map(int, input().split()))
graph = {}; attacked = {i : False for i in range(comps)}; attacked[comps - 1] = True; bad = False; way = [comps - 1]
for _ in range(nets):
    u, v = list(map(int, input().split()))
    if u in graph.keys():
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph.keys():
        graph[v].append(u)
    else:
        graph[v] = [u]
while not attacked[0]:
    node = way[-1]
    for n in [neighbor for neighbor in graph[node] if not attacked[neighbor]]:
        if min_attacked[n] <= count_attacked(n, graph, attacked):
            way.append(n); attacked[n] = True; break
    else:
        if node == comps - 1:
            bad = True; break
        way.pop()
print('YES' if not bad else 'NO')