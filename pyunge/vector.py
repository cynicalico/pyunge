import array


class Vector:
    def __init__(self, reserve, *, fill_reverse, dtype="f"):
        self.fill_reverse = fill_reverse
        self.dtype = dtype

        self.data = array.array(self.dtype, [0] * reserve)
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

    def front(self):
        if self.fill_reverse:
            return self.pos
        return 0

    def back(self):
        if self.fill_reverse:
            return self.cap
        return self.pos

    def size(self):
        if self.fill_reverse:
            return self.cap - self.pos
        return self.pos
    
    def capacity(self):
        return len(self.data)

    def clear(self):
        self.pos = self.cap if self.fill_reverse else 0

    def add(self, new_data):
        if type(new_data) == list:
            new_data = array.array(self.dtype, new_data)

        while self.should_grow_(new_data):
            self.grow_(self.cap * 2)
            if self.fill_reverse:
                old_size = (self.cap // 2) - self.pos
                old_pos = self.pos
                self.pos = self.cap - old_size
                self.data[self.pos :] = self.data[old_pos : old_pos + old_size]

        l = self.pos
        if self.fill_reverse:
            l -= len(new_data)
        self.data[l : l + len(new_data)] = new_data

        if self.fill_reverse:
            self.pos -= len(new_data)
        else:
            self.pos += len(new_data)
