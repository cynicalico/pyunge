from pyunge.vector import Vector
import moderngl as mgl
import array


class VBuffer:
    def __init__(self, ctx: mgl.Context, size, fill_reverse):
        self.ctx = ctx
        self.fill_reverse = fill_reverse

        self.vec = Vector(size, fill_reverse=fill_reverse)

        self.buf = self.ctx.buffer(reserve=size * self.vec.data.itemsize, dynamic=True)
        self.bufpos = 0

    def clear(self):
        self.vec.clear()
        self.bufpos = self.vec.front() if self.fill_reverse else self.vec.back()

    def add(self, new_data):
        self.vec.add(new_data)

    def sync(self):
        if self.buf.size // self.vec.data.itemsize < self.vec.size():
            while self.buf.size // self.vec.data.itemsize < self.vec.size():
                self.buf.orphan(self.vec.capacity() * self.vec.data.itemsize)
            self.buf.write(self.vec.data)
            self.bufpos = self.vec.front() if self.fill_reverse else self.vec.back()
        else:
            if self.fill_reverse and self.bufpos > self.vec.front():
                self.buf.write(
                    self.vec.data[
                        self.vec.front() : self.vec.front()
                        + (self.bufpos - self.vec.front())
                    ],
                    self.vec.front() * self.vec.data.itemsize,
                )
                self.bufpos = self.vec.front()
            elif not self.fill_reverse and self.bufpos < self.vec.back():
                self.buf.write(
                    self.vec.data[self.bufpos :], self.bufpos * self.vec.data.itemsize
                )
                self.bufpos = self.vec.back()
