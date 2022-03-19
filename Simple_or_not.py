from math import sqrt
alpha = int(input('Введите число: '))
def is_simple(alpha):
	for i in range(2, int(sqrt(alpha)) + 1):
		if alpha % i == 0:
			print('Составное')
			break
	else:
		print('Простое')
is_simple(alpha)	
input('Press enter to exit')			