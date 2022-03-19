def get_winner(elections):
	'''Принимает на вход словарь вида {кандидат : колво голосов} и возвращает имя победителя'''
	elections = {name : votes for name, votes in elections.items() if votes == max(elections.values())}	
	return sorted(elections.items(), key = lambda x : x[0])

def advanced_sorting(alpha):
	'''Принимает на вход словарь, сортирует в первую очередь по значениям, а потом
	повторяющиеся в лексикографическом порядке'''
	while len(alpha) != 0:
		for tup in get_winner(alpha): del alpha[tup[0]]; yield tup[0] + ' ' + str(tup[1])

states_electors = {}
states_candidates_votes = {}
result = {}
for _ in range(int(input())):
	alpha = input().split()
	states_electors[alpha[0]] = int(alpha[1])
	states_candidates_votes[alpha[0]] = {}
for _ in range(int(input())):
	alpha = input().split()
	states_candidates_votes[alpha[0]][alpha[1]] = states_candidates_votes[alpha[0]].get(alpha[1], 0) + 1
	result[alpha[1]] = 0

for item in states_candidates_votes:
	result[get_winner(states_candidates_votes[item])[0][0]] += states_electors[item]

print('\n'.join(advanced_sorting(result)))	

input('Press enter to exit: ')