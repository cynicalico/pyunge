import copy
import random

from pyunge.engine.instruction_mapping import InstructionMapping
from pyunge.engine.stackstack import StackStack


class InstructionPointer:
    def __init__(self, *, pos=None, delta=None):
        self.pos = pos or [0, 0]
        self.saved_pos = None
        self.delta = delta or [0, 1]
        self.saved_delta = None
        self.alive = True
        self.stringmode = False
        self.stack = StackStack()
        self.storage_offset = [0, 0]
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

    def save_pos(self):
        self.saved_pos = copy.copy(self.pos)

    def restore_pos(self):
        self.pos = copy.copy(self.saved_pos)

    def save_delta(self):
        self.saved_delta = copy.copy(self.delta)

    def restore_delta(self):
        self.delta = copy.copy(self.saved_delta)

    def begin_block(self):
        self.stack.begin_block(self.storage_offset)
        self.storage_offset = [self.pos[0] + self.delta[0], self.pos[1] + self.delta[1]]

    def end_block(self):
        success, restored_storage_offset = self.stack.end_block()
        if not success:
            self.reverse()
        else:
            self.storage_offset = restored_storage_offset

    def stack_under_stack(self):
        if not self.stack.stack_under_stack():
            self.reverse()

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
