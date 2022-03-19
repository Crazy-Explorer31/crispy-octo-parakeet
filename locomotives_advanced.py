max_min = int(input())
way = list(map(int, input().split()))
stack = []; now_min = 1; flag = True; countdown = []
while True:
	temp1 = 0; temp2 = 0
	for i in way:
		if i > now_min:
			stack.append(i)
			temp1 += 1
		else:
			stack.append(i)
			temp1 += 1; break
	for i in range(temp1): del way[0]
	for i in stack[::-1]:
		if i == now_min: 
			now_min += 1; temp2 += 1
		else: break
	for i in range(temp2): stack.pop()	
	countdown.extend(['1' + ' ' + str(temp1), '2' + ' ' + str(temp2)])	
	if now_min in stack:
		flag = not flag; break
	if len(way) == 0: break	
print('\n'.join(countdown)) if flag else print(0)