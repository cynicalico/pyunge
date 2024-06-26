from pyunge.engine.errors import GnirtsError


class StackStack:
    def __init__(self):
        self.stacks = [[]]
        self.toss = 0
        self.soss = None

    def push(self, v):
        self.push_(v, self.toss)

    def push_(self, v, i):
        self.stacks[i].append(v)

    def extend_(self, vs, i=None):
        i = self.toss if i is None else i
        self.stacks[i].extend(vs)

    def pop(self):
        return self.pop_(self.toss)

    def pop_(self, i):
        if len(self.stacks[i]) == 0:
            return 0
        return self.stacks[i].pop()

    def pop_vector(self, ip=None):
        r = self.pop()
        c = self.pop()
        if ip is not None:
            r += ip.storage_offset[0]
            c += ip.storage_offset[1]
        return r, c

    def pop_0gnirts(self):
        s = ''
        while True:
            c = self.pop()
            if c == ord('\0'):
                break
            try:
                s += chr(c)
            except ValueError as e:
                raise GnirtsError(f"Failed to convert value '{c}' to char while popping 0gnirts")
        return s

    def duplicate(self):
        v = self.pop()
        self.push(v)
        self.push(v)

    def swap(self):
        v1 = self.pop()
        v2 = self.pop()
        self.push(v1)
        self.push(v2)

    def clear(self):
        self.stacks[self.toss].clear()

    def pick(self, n):
        n = len(self.stacks[self.toss]) - n
        if n < len(self.stacks[self.toss]):
            return self.stacks[self.toss][n]
        return 0

    def begin_block(self, storage_offset):
        n = self.pop()

        self.stacks.append([])
        self.toss += 1
        self.soss = self.toss - 1

        if n > 0:
            soss_len = len(self.stacks[self.soss])
            zero_fill = n - soss_len
            if zero_fill > 0:
                self.extend_([0] * zero_fill)
                n -= zero_fill
            self.stacks[self.soss], transfer = \
                self.stacks[self.soss][:soss_len - n], self.stacks[self.soss][soss_len - n:]
            self.extend_(transfer)

        else:
            for _ in range(abs(n)):
                self.push_(0, self.soss)

        self.extend_(storage_offset, self.soss)

    def end_block(self):
        if self.soss is None:
            return False, [0, 0]

        n = self.pop()
        storage_offset_c = self.pop_(self.soss)
        storage_offset_r = self.pop_(self.soss)

        if n > 0:
            toss_len = len(self.stacks[self.toss])
            transfer = self.stacks[self.toss][max(0, toss_len - n):]
            self.extend_(transfer, self.soss)

        else:
            for _ in range(abs(n)):
                self.pop_(self.soss)

        self.stacks.pop()
        self.toss -= 1
        self.soss = None if self.toss == 0 else self.toss - 1

        return True, [storage_offset_r, storage_offset_c]

    def stack_under_stack(self):
        if self.soss is None:
            return False

        n = self.pop()
        src = self.soss
        dst = self.toss

        if n < 0:
            src = self.toss
            dst = self.soss
            n = abs(n)

        # TODO: Make this do a slice assignment instead,
        #       this is really inefficient
        for _ in range(n):
            self.push_(self.pop_(src), dst)

        return True
