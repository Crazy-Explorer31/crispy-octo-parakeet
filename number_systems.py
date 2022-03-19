def from_base_to_dec(value, base):
	res = 0
	for i in range(len(value)):
		res += int(value[i]) * base**i
	return str(res)
def from_dec_to_base(value, base):
	value = int(value); res = str(value % base)
	while value > 0:
		value //= base
		res = str(value % base) + res
	return res