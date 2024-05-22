import random
from .instruction_mapping import InstructionMapping
from .stackstack import StackStack


class InstructionPointer:
    def __init__(self, *, pos=None, delta=None):
        self.pos = pos or [0, 0]
        self.delta = delta or [0, 1]
        self.alive = True
        self.stringmode = False
        self.stack = StackStack()
        self.instruction_mapping = InstructionMapping()

    def step_(self):
        self.pos[0] += self.delta[0]
        self.pos[1] += self.delta[1]

    def step(self, fs):
        self.step_()
        if not fs.in_bounds(*self.pos):
            self.wrap(fs)

    def move(self, last_ins, fs):
        skipping = False

        while True:
            self.step(fs)
            ins = fs.get(*self.pos)

            if self.stringmode:
                if skipping:
                    if ins != ord(' '):
                        skipping = False
                elif ins == ord(' ') and last_ins == ord(' '):
                    skipping = True
                    continue

            elif not skipping:
                if ins == ord(';'):
                    skipping = True
                    continue
                if ins == ord(' '):
                    continue

            elif skipping:
                if ins == ord(';'):
                    skipping = False
                continue

            break

    def wrap(self, fs):
        self.reverse()
        self.step_()
        while fs.in_bounds(*self.pos):
            self.step_()
        self.reverse()
        self.step_()

    def absolute_vector(self, delta):
        self.delta = delta

    def go_north(self):
        self.absolute_vector([-1, 0])

    def go_south(self):
        self.absolute_vector([1, 0])

    def go_east(self):
        self.absolute_vector([0, 1])

    def go_west(self):
        self.absolute_vector([0, -1])

    def go_away(self):
        opts = [self.go_north, self.go_south, self.go_east, self.go_west]
        opts[random.randint(0, len(opts) - 1)]()

    def turn_right(self):
        self.delta = [self.delta[1], -self.delta[0]]

    def turn_left(self):
        self.delta = [-self.delta[1], self.delta[0]]

    def reverse(self):
        self.delta = [-self.delta[0], -self.delta[1]]
