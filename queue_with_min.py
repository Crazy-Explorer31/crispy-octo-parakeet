stack1 = []; stack_of_mins1 = []; stack2 = []; stack_of_mins2 = []
for _ in range(int(input())):
	alpha = int(input())
	if alpha > 0:
		stack1.append(alpha)
		if not stack_of_mins1 or alpha < stack_of_mins1[-1]:
			stack_of_mins1.append(alpha)
		else:
			stack_of_mins1.append(stack_of_mins1[-1])
	else:
		if not stack2 and not stack1:
			print(-1)		
		elif not stack2 and stack1:
			for _ in range(len(stack1)):
				if not stack_of_mins2 or stack1[-1] < stack_of_mins2[-1]:
					stack_of_mins2.append(stack1[-1])
				else:
					stack_of_mins2.append(stack_of_mins2[-1])
				stack2.append(stack1.pop())
			stack_of_mins1 = []	
			print(stack_of_mins2.pop()); stack2.pop()
		elif stack_of_mins1:
			stack2.pop()
			print(min(stack_of_mins1[-1], stack_of_mins2.pop()))
		else:
			stack2.pop(); print(stack_of_mins2.pop())