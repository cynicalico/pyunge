import numpy as np


class Vector:
    def __init__(self, reserve, *, fill_reverse):
        self.fill_reverse = fill_reverse

        self.data = np.zeros(reserve)
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
