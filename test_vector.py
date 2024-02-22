from pyunge.vector import Vector
import numpy as np
import time


def py_arr(a):
    a.clear()
    for i in range(1000):
        a.extend([1, 2, 3, 1, 2, 3, 1, 2, 3])


def np_vec(a):
    a.clear()
    for i in range(1000):
        a.add(np.array([1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0]))


if __name__ == '__main__':
    # v = Vector(1, fill_reverse=True)

    # v.add([1, 2, 3])
    # v.add([4, 5, 6])
    # v.add([7, 8])

    # print(v.data)

    a = []
    t1 = time.time()
    for _ in range(1000):
        py_arr(a)
    t2 = time.time()
    print(t2 - t1)

    a = Vector(1, fill_reverse=False)
    t1 = time.time()
    for _ in range(1000):
        np_vec(a)
    t2 = time.time()
    print(t2 - t1)
