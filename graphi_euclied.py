graph = {'a' : {'b', 'c'}, 'b' : {'a', 'c'}, 'c' : {'a', 'd', 'e'}, 'd' : {'c'}, 'e' : {'c'}}
def DFS(graph):
	'''returns way by that depth_first search algorithm walk by this gragh'''
	status = {i : 0 for i in sorted(graph.keys())} # 0 - if we didn't visit this vertex and 1 else
	path = [sorted(graph.keys())[0]]
	while path:
		print(path[-1], end = ' ')
		status[path[-1]] = 1
		for i in graph[path[-1]]:
			if status[i] == 0:
				path.append(i)
				break
		else:
			path.pop()

from collections import deque			
def BFS(graph, start, finish):
	'''returns shortest way from start to finish in unweighted graph and its length'''
	queue = deque(); queue.append(start); prev = {i : None for i in graph.keys()}; res_way = []
	while True:
		grand = queue.popleft(); temp = graph[grand]
		if finish in temp:
			prev[finish] = grand
			break
		else:
			for j in temp:
				prev[j] = grand
			queue.extend(temp)
	part_of_way = finish		
	while True:
		res_way.append(part_of_way)
		if prev[part_of_way] == None:
			break
		part_of_way = prev[part_of_way]
	return (res_way[::-1], len(res_way))
graph1 = {'a' : {'b' : 2, 'c' : 3}, 'b' : {'a' : 2, 'c' : 1}, 'c' : {'a' : 3, 'd' : 2, 'e' : 4}, \
	'd' : {'c' : 2}, 'e' : {'c' : 4}} #weighted
def deikstra(graph, start, finish):
	dists = {i : float('inf') for i in graph.keys()}; dists[start] = 0; visited = set()
	def find_next(graph, dists, visited):
		res_node = None; res_length = float('inf')
		for suspect in (set(graph.keys()) - visited):
			if dists[suspect] < res_length:
				res_length = dists[suspect]; res_node = suspect
		return res_node		

	node = start; visited.add(node)
	while (set(graph.keys()) - visited):
		for n in [j for j in graph[node] if j not in visited]:
			if dists[n] > dists[node] + graph[node][n]:
				dists[n] = dists[node] + graph[node][n]
		node = find_next(graph, dists, visited)
		visited.add(node)	
	node = finish; res_way = [finish]; s_dist = dists[finish]
	while True:
		for i in [j for j in graph.keys() if node in graph[j]]:
			if dists[i] == dists[node] - graph[i][node]:
				s_dist -= graph[i][node]; node = i; res_way.append(i); break
		if node == start:
			break		
	return res_way[::-1], dists[finish]

def	full_euclied(a, b):
	if a == 0:
		return b, 0, 1
	else:
		d, x, y = full_euclied(b % a, a)
		return d, y - (b // a) * x, x 
def solve_diofant(a, b, c):
	'''ax + by = c => x, x_step, y, y_step'''
	d, x0, y0 = full_euclied(abs(a), abs(b))
	if c % d != 0:
		return 'no solutions'
	else:
		x1, y1 = x0 * (c // d), y0 * (c // d) 
		if (a < 0 and b > 0 and c >= 0) or (a > 0 and b < 0 and c <= 0):
			return -x1, b // d, y1, a // d
		elif (a > 0 and b < 0 and c >= 0) or (a < 0 and b > 0 and c <= 0):
			return x1, b // d, -y1, a // d	
		elif (a > 0 and b > 0 and c < 0) or (a < 0 and b < 0 and c > 0):
			return -x1, b // d, -y1, a // d	
		else:
			return x1, b // d, y1, a // d