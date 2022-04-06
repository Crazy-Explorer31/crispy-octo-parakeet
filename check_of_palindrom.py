alpha = list(input()); f = lambda x : int((x & 1) ^ 1); res = True
for i, j in zip(range(len(alpha) >> 1), range(len(alpha) - 1, (len(alpha) >> 1) - f(len(alpha)), -1)):
    if '?' in alpha[i] + alpha[j]:
        if alpha[i] == alpha[j] == '?':
            alpha[i] = 'a'; alpha[j] = 'a'
        elif alpha[i] == '?':
            alpha[i] = alpha[j]
        elif alpha[j] == '?':
            alpha[j] = alpha[i]
    elif alpha[i] != alpha[j]:
        res = False; break
if len(alpha) & 1:
    if alpha[len(alpha) >> 1] == '?':
        alpha[len(alpha) >> 1] = 'a'
if res:
    print('YES', ''.join(alpha), sep = '\n')
else:
    print('NO')

