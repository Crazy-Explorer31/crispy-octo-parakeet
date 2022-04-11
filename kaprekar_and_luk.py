import numpy as np
def kaprekar_loop(n):
    if n in {1000, 100, 100000} or len(set(list(str(n)))) == 1:
        print(f'Ошибка! На вход подано число {n}, не удовлетворяющее условиям процесса Капрекара')
    else:
        res = [n]; flag = False
        while not n in {495, 6174, 549945, 631764}:
            alpha = list(map(int, list(str(n)))); alpha.sort()
            n = int(''.join(map(str, alpha[::-1]))) - int(''.join(map(str, alpha)))
            if n in res:
                res.append(n); flag = True; break
            res.append(n)
        if flag:
            res[-1] = f'Следующее число - {res[-1]}, кажется процесс зациклился...'
            print('\n'.join(map(str, res)))
        else:
            print('\n'.join(map(str, res)))

def find_luk(n):
    def matr_power(matr, k):
        res = np.array([[1, 0], [0, 1]])
        while k:
            if k & 1:
                res = np.dot(res, matr); k -= 1
            matr = np.dot(matr, matr); k >>= 1
        return res
    aggregate_matrix = matr_power(np.array([[0, 1], [1, 1]]), n)
    return np.dot(np.array([[2, 1]]), aggregate_matrix)[0, 0]
