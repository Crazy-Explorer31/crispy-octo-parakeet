x1, y1, x3, y3 = [int(i) for i in input().split()]
x3, y3 = abs(x1 - x3), abs(y1 - y3)
if x3 == 0 or y3 == 0:
	print(0)
else:	
	def get_simples(a, b):
		def gcd(a, b):
			if b == 0:
				return a 
			return gcd(b, a % b)					
		res = gcd(max(a, b), min(a, b))
		return (int(a / res), int(b / res)) 
	y_moving, x_moving = get_simples(y3, x3)
	preference = x3 // x_moving
	print(preference * (y_moving + x_moving - 1))