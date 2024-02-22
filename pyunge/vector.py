import array
import numpy as np


class PyBuf:
    def __init__(self, *, fill_reverse):
        self.fill_reverse = fill_reverse
        self.data = []

    def clear(self):
        self.data.clear()

    def add(self, new_data):
        if self.fill_reverse:
            self.data = new_data + self.data
        else:
            self.data.extend(new_data)


class ArrBuf:
    def __init__(self, reserve, *, fill_reverse):
        self.fill_reverse = fill_reverse

        self.data = array.array('f', [0] * reserve)
        self.cap = reserve
        self.clear()

    def should_grow_(self, new_data):
        if self.fill_reverse:
            return self.pos - len(new_data) < 0
        else:
            return self.pos + len(new_data) > self.cap
        
    def grow_(self, new_cap):
        self.cap = new_cap
        self.data.extend([0] * (self.cap - len(self.data)))
        
    def clear(self):
        self.pos = self.cap if self.fill_reverse else 0

    def add(self, new_data):
        while self.should_grow_(new_data):
            self.grow_(self.cap * 2)
            if self.fill_reverse:
                old_size = (self.cap // 2) - self.pos
                old_pos = self.pos
                self.pos = self.cap - old_size
                self.data[self.pos:] = self.data[old_pos:old_pos+old_size]

        l = self.pos
        if self.fill_reverse:
            l -= len(new_data)
        self.data[l : l + len(new_data)] = new_data

        if self.fill_reverse:
            self.pos -= len(new_data)
        else:
            self.pos += len(new_data)



class NpBuf:
    def __init__(self, reserve, *, fill_reverse):
        self.fill_reverse = fill_reverse

        self.data = np.empty(reserve)
        self.cap = reserve
        self.clear()

    def should_grow_(self, new_data):
        if self.fill_reverse:
            return self.pos - len(new_data) < 0
        else:
            return self.pos + len(new_data) > self.cap
        
    def clear(self):
        self.pos = self.cap if self.fill_reverse else 0

    def add(self, new_data):
        while self.should_grow_(new_data):
            self.cap *= 2
            self.data.resize(self.cap, refcheck=False)
            if self.fill_reverse:
                old_size = (self.cap // 2) - self.pos
                old_pos = self.pos
                self.pos = self.cap - old_size
                self.data[self.pos:] = self.data[old_pos:old_pos+old_size]

        l = self.pos
        if self.fill_reverse:
            l -= len(new_data)
        self.data[l : l + len(new_data)] = new_data

        if self.fill_reverse:
            self.pos -= len(new_data)
        else:
            self.pos += len(new_data)
