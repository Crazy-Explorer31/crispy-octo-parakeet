import numpy as np
def modify_matr(X, y, degree):
        new_y = y.reshape((y.shape[0], 1))
        new_X = X.copy(); new_X = np.concatenate([np.ones(new_y.shape), new_X], axis=1); j_paste = 1
        for j in range(1, new_X.shape[1]):
            temp_matrix = X[:, (j - 1)].reshape(new_y.shape)
            for c in range(degree - 1):
                temp_matrix = np.concatenate([temp_matrix, np.multiply(
                    temp_matrix[:, 0].reshape(new_y.shape), temp_matrix[:, c:])],
                                             axis=1)
            new_X = np.concatenate([new_X[:, 0:j_paste], temp_matrix,
                                    new_X[:, (j_paste + degree):]], axis=1); j_paste += degree
    return new_X
X = np.array([[1], [3], [12]]); y = np.array([34, 27, 8]); degree = 3
print(modify_matr(X, y, degree))