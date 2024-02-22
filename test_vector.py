from pyunge.vector import Vector
import numpy as np
import time
import array


def py_arr_arr(a):
    a.clear()
    for _ in range(30000):
        a.add(array.array("f", [1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0]))


def bench(a, f):
    t1 = time.time()
    for _ in range(60):
        f(a)
    t2 = time.time()
    print(t2 - t1)


if __name__ == "__main__":
    a = Vector(1, fill_reverse=False)
    bench(a, py_arr_arr)

    a = Vector(1, fill_reverse=True)
    bench(a, py_arr_arr)
    