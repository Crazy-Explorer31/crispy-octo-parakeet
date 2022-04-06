from sys import stdout
i = 1; res = '! '; res_count = 0; first_res = None
while res_count == 0:
    print(f'? {i}'); k = int(input()); stdout.flush()
    if k == 1:
        res += str(i) + ' '; res_count += 1; first_res = i
    elif k == 2:
        res += str(i) + ' ' + str(i); res_count += 2
    i += 1

while res_count < 2:
    print(f'? {i}'); k = int(input()); stdout.flush()
    if (k == 1 and i % first_res != 0) or (k == 2 and i % first_res == 0):
        res += str(i); res_count += 1; break
    i += 1
print(res)
