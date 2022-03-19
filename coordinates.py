x_coords = []; y_coords = []
for _ in range(int(input())):
	x, y = map(int, input().split())
	x_coords.append(x + 0.5); y_coords.append(y + 0.5) 	

y_directs = [int(i + 0.5) for i in sorted(list(set(y_coords)))[:-1]] #горизонтальные прострелы

x_coords = [x_coords[i] for i in range(len(y_coords)) if y_coords.count(y_coords[i]) != 1]

x_directs = [int(i + 0.5) for i in sorted(list(set(x_coords)))[:-1]] #вертикальные прострелы

print(len(x_directs) + len(y_directs))
for y in y_directs: print('y', y)
for x in x_directs: print('x', x)