from pyunge.vector import PyBuf, ArrBuf, NpBuf
import numpy as np
import time
import array


def py_arr(a):
    a.clear()
    for _ in range(10000):
        a.add([1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0])
    np.array(a.data)


def py_arr_arr(a):
    a.clear()
    for _ in range(10000):
        a.add(array.array("f", [1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0]))


def np_vec(a):
    a.clear()
    for _ in range(10000):
        a.add([1.0, 2.0, 3.0, 1.0, 2.0, 3.0, 1.0, 2.0, 3.0])


def bench(a, f):
    t1 = time.time()
    for _ in range(60):
        f(a)
    t2 = time.time()
    print(t2 - t1)


if __name__ == "__main__":
    print("Forwards")
    a = PyBuf(fill_reverse=False)
    bench(a, py_arr)

    a = ArrBuf(1, fill_reverse=False)
    bench(a, py_arr_arr)

    a = NpBuf(1, fill_reverse=False)
    bench(a, np_vec)

    print("Reverse")
    a = PyBuf(fill_reverse=True)
    bench(a, py_arr)

    a = ArrBuf(1, fill_reverse=True)
    bench(a, py_arr_arr)

    a = NpBuf(1, fill_reverse=True)
    bench(a, np_vec)