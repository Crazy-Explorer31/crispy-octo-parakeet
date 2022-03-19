def modify_queue(queue, first_index):
	if len(queue) - first_index <= first_index:
		for i in range(first_index): del queue[0]; first_index = 0
	return first_index	

def motion(alpha1, alpha2, first_index1, first_index2):
	temp = [alpha1[first_index1], alpha2[first_index2]]
	if alpha1[first_index1] == 0 and alpha2[first_index2] == 9:
		first_index1 += 1
		alpha1.extend(temp)
		first_index1 = modify_queue(alpha1, first_index1)

		first_index2 += 1
		first_index2 = modify_queue(alpha2, first_index2)
	elif alpha1[first_index1] == 9 and alpha2[first_index2] == 0:
		first_index1 += 1
		first_index1 = modify_queue(alpha1, first_index1)

		first_index2 += 1
		alpha2.extend(temp)
		first_index2 = modify_queue(alpha2, first_index2)
	else:
		if alpha1[first_index1] > alpha2[first_index2]:
			first_index1 += 1
			alpha1.extend(temp)
			first_index1 = modify_queue(alpha1, first_index1)

			first_index2 += 1
			first_index2 = modify_queue(alpha2, first_index2)
		else:
			first_index1 += 1
			first_index1 = modify_queue(alpha1, first_index1)

			first_index2 += 1
			alpha2.extend(temp)
			first_index2 = modify_queue(alpha2, first_index2)	

	return (first_index1, first_index2)			

alpha1 = list(map(int, input().split())); first_index1 = 0
alpha2 = list(map(int, input().split())); first_index2 = 0
count_of_motions = 0
for i in range(10**6):
	if not alpha1 or not alpha2 or first_index1 == len(alpha1) or first_index2 == len(alpha2):
		if not alpha1 or first_index1 == len(alpha1):
			print('second', count_of_motions)
		else:
			print('first', count_of_motions)	
		break
	first_index1, first_index2 = motion(alpha1, alpha2, first_index1, first_index2)
	count_of_motions += 1
else:	
	print('botva')