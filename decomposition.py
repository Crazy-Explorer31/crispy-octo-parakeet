def factorization(n):
	divisiors = []
	base_div = 2
	while base_div**2 <= n:
		while n % base_div == 0:
			divisiors.append(base_div)
			n //= base_div
		base_div += 1
	if n > 1:
		divisiors.append(n)	
	return divisiors	
obj = factorization(int(input()))
pref = '*'.join([str(i) + '^' + str(j) if j > 1 else str(i) + '' 
	for i, j in zip(list(set(obj)), [obj.count(i) for i in set(obj)])])
print(pref)