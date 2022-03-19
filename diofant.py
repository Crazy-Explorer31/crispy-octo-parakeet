def gcd(a, b):
	if b == 0:
		return a 
	return gcd(b, a%b)	
def reduction(a, b):
	global gcd
	d = gcd(a, b)
	return [a // d, b // d]
a, b, c = [int(i) for i in input().split()]
if c % gcd(max(a, b), min(a, b)) != 0:
	print(-1)
else:
	def gcd_ext(a, b):
		'''Returns gcd(a, b); x and y, satisfying equation a*x + b*y = gcd(a, b)'''
		if b == 0:
			return a, 1, 0
		d, x, y = gcd_ext(b, a % b)
		x, y = y, x - (a // b) * y
		return d, x, y
	d, p_x, p_y = gcd_ext(a, b)	
	p_x *= c // d	
	b_moving = abs(b // d)
	if p_x % b_moving == 0:
		print(0, c//b)
	elif p_x > 0:
		x = p_x % b_moving	
		y = (c - a*x) // b
		print(x, y)
	else:
		x = -(abs(p_x) % b_moving) + b_moving
		y = (c - a*x) // b 
		print(x, y)
input('Press enter to exit')