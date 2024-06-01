from collections.abc import Iterable


def flatten(xs):
    for x in xs:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x


class SwapList:
    def __init__(self):
        self.l1_ = []
        self.l2_ = []
        self.ind = False

    def active_list(self):
        if not self.ind:
            return self.l1_
        return self.l2_

    def inactive_list(self):
        if not self.ind:
            return self.l2_
        return self.l1_

    def swap_active(self):
        self.ind = not self.ind

    def __len__(self):
        if not self.ind:
            return len(self.l1_)
        return len(self.l2_)
