operations = {'+' : lambda x, y : x + y, '-' : lambda x, y : x - y, '*' : lambda x, y : x*y}
expression = input().split()
stack = []
for item in expression:
	if item not in '+-*':
		stack.append(int(item))
	else:
		temp = operations[item](stack[-2], stack[-1])
		stack.pop(); stack.pop()
		stack.append(temp)
print(stack[0])