import numpy as np

def get_fibo(n):
    base = np.array([[0, 1], [1, 1]])
    return np.dot(np.array([[1, 1]]), binpow(base, n))[0][0]

def binpow(a, n):
    res = np.array([[1, 0], [0, 1]])
    while n:
        if n & 1:
            res = np.dot(res, a); n -= 1
        a = np.dot(a, a); n >>= 1
    return res

print(get_fibo(5))