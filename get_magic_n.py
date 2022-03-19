def factorization(n):
	p = 2; divisiors = {}
	while p**2 <= n:
		if n % p == 0:
			temp = 0
			while n % p == 0:
				n //= p; temp += 1
			divisiors[p] = temp
		p += 1
	if n != 1:
		divisiors[n] = 1
	return divisiors	

a, b = list(map(int, input().split()))
a_divisiors, b_divisiors = factorization(a), factorization(b)
a_divisiors.update({i : 0 for i in set(b_divisiors.keys()) - set(a_divisiors.keys())})
b_divisiors.update({i : 0 for i in set(a_divisiors.keys()) - set(b_divisiors.keys())})
res = 1
for p in a_divisiors.keys():
	if a_divisiors[p] % 2 == 0:
		if b_divisiors[p] % 3 == 1:
			res *= p**2
		elif b_divisiors[p] % 3 == 2:
			res *= p**4
	elif a_divisiors[p] % 2 == 1:
		if b_divisiors[p] % 3 == 0:
			res *= p**3
		elif b_divisiors[p] % 3 == 1:
			res *= p**5
		elif b_divisiors[p] % 3 == 2:
			res *= p 	
print(f'n = {res}\na*n = {a * res} = {int((a * res) ** 0.5)}^2; b*n = {b * res} = {round((b * res) ** (1 / 3))}^3')
# n : a * n = x^2, x - N; b * n = y^3, y - N