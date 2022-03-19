words_variants = {}
for _ in range(int(input())):
	info = input()
	if info.lower() in words_variants.keys():
		words_variants[info.lower()].add(info)
	else:
		words_variants[info.lower()] = {info}
errors = 0		
for item in input().split():
	if item.lower() not in words_variants.keys():
		if not (len([i for i in item if 65 <= ord(i) <= 90]) == 1):
			errors += 1
		else: continue
	elif not (item in words_variants[item.lower()]):
		errors += 1		
print(errors)