from random import randrange
def get_element_position_cycled(array, alpha):
	left = 0; right = len(array) - 1
	while left <= right:
		middle = (left + right) // 2
		if array[middle] < alpha:
			left = middle + 1
		elif array[middle] > alpha:
			right = middle - 1
		else:
			return middle
	return None	

def get_element_position_recoursive(array, alpha, left = None, right = None):
	if left == right == None:
		left, right = 0, len(array) - 1 
	if left > right:
		return None
	middle = (left + right) // 2
	if array[middle] == alpha:
		return middle
	else:
		return get_element_position_recoursive(array, alpha, middle + 1, right) if array[middle] < alpha else \
			get_element_position_recoursive(array, alpha, left, middle - 1)

def get_sorted_sequence(array):	
	if len(array) < 2:
		return array
	else:
		support = array.pop(randrange(0, len(array)))
		part1 = [i for i in array if i < support]
		part2 = [i for i in array if i >= support]
		return get_sorted_sequence(part1) + [support] + get_sorted_sequence(part2)
