import moderngl as mgl
import array


class VBuffer:
    def __init__(self, ctx: mgl.Context, size, *, fill_reverse, dtype="f"):
        self.ctx = ctx
        self.fill_reverse = fill_reverse
        self.dtype = dtype

        self.data = array.array(self.dtype, [0] * size)
        self.cap = size

        self.buf = self.ctx.buffer(reserve=size * self.data.itemsize, dynamic=True)

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
        self.bufpos = self.front() if self.fill_reverse else self.back()

    def add(self, new_data):
        if type(new_data) == list:
            new_data = array.array(self.dtype, new_data)

        while self.should_grow_(new_data):
            self.grow_(self.cap * 2)
            if self.fill_reverse:
                old_size = (self.cap // 2) - self.pos
                old_pos = self.pos
                self.pos = self.cap - old_size
                self.data[self.pos:] = self.data[old_pos: old_pos + old_size]

        l = self.pos
        if self.fill_reverse:
            l -= len(new_data)
        self.data[l: l + len(new_data)] = new_data

        if self.fill_reverse:
            self.pos -= len(new_data)
        else:
            self.pos += len(new_data)

    def sync(self):
        if self.buf.size // self.data.itemsize < self.size():
            while self.buf.size // self.data.itemsize < self.size():
                self.buf.orphan(self.capacity() * self.data.itemsize)
            self.buf.write(self.data)
            self.bufpos = self.front() if self.fill_reverse else self.back()
        elif self.fill_reverse and self.bufpos > self.front():
            unbuf_size = self.bufpos - self.front()
            self.buf.write(
                self.data[self.front(): self.front() + unbuf_size],
                self.front() * self.data.itemsize,
            )
            self.bufpos = self.front()
        elif not self.fill_reverse and self.bufpos < self.back():
            self.buf.write(self.data[self.bufpos:], self.bufpos * self.data.itemsize)
            self.bufpos = self.back()
