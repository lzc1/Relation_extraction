import numpy as  np


def matrix_combine(a,b):
     return np.column_stack((a,b))


if __name__ == '__main__':
    a = np.zeros((3,3))
    print(a)
    b = np.ones((3,5))
    c = matrix_combine(a,b)
    print(c.shape)
    print(c)