import enum


class InstructionResult(enum.Enum):
    NONE = enum.auto()
    KILL = enum.auto()
    SPLIT = enum.auto()
    QUIT = enum.auto()
    ITER = enum.auto()


class InstructionMapping:
    def __init__(self):
        self.mapping = {
            # ord(' '): self.empty_,
            ord('!'): self.logical_not_,
            ord('"'): self.toggle_stringmode_,
            ord('#'): self.trampoline_,
            ord('$'): self.pop_,
            ord('%'): self.remainder_,
            ord('&'): self.input_integer_,
            ord('\''): self.fetch_character_,
            ord('('): self.load_semantics_,
            ord(')'): self.unload_semantics_,
            ord('*'): self.multiply_,
            ord('+'): self.add_,
            ord(','): self.output_character_,
            ord('-'): self.subtract_,
            ord('.'): self.output_integer_,
            ord('/'): self.divide_,
            ord('0'): self.push_zero_,
            ord('1'): self.push_one_,
            ord('2'): self.push_two_,
            ord('3'): self.push_three_,
            ord('4'): self.push_four_,
            ord('5'): self.push_five_,
            ord('6'): self.push_six_,
            ord('7'): self.push_seven_,
            ord('8'): self.push_eight_,
            ord('9'): self.push_niner_,
            ord(':'): self.duplicate_,
            # ord(';'): self.jump_over_,
            ord('<'): self.go_west_,
            ord('='): self.execute_,
            ord('>'): self.go_east_,
            ord('?'): self.go_away_,
            ord('@'): self.stop_,
            ord('A'): self.fingerprint_defined_,
            ord('B'): self.fingerprint_defined_,
            ord('C'): self.fingerprint_defined_,
            ord('D'): self.fingerprint_defined_,
            ord('E'): self.fingerprint_defined_,
            ord('F'): self.fingerprint_defined_,
            ord('G'): self.fingerprint_defined_,
            ord('H'): self.fingerprint_defined_,
            ord('I'): self.fingerprint_defined_,
            ord('J'): self.fingerprint_defined_,
            ord('K'): self.fingerprint_defined_,
            ord('L'): self.fingerprint_defined_,
            ord('M'): self.fingerprint_defined_,
            ord('N'): self.fingerprint_defined_,
            ord('O'): self.fingerprint_defined_,
            ord('P'): self.fingerprint_defined_,
            ord('Q'): self.fingerprint_defined_,
            ord('R'): self.fingerprint_defined_,
            ord('S'): self.fingerprint_defined_,
            ord('T'): self.fingerprint_defined_,
            ord('U'): self.fingerprint_defined_,
            ord('V'): self.fingerprint_defined_,
            ord('W'): self.fingerprint_defined_,
            ord('X'): self.fingerprint_defined_,
            ord('Y'): self.fingerprint_defined_,
            ord('Z'): self.fingerprint_defined_,
            ord('['): self.turn_left_,
            ord('\\'): self.swap_,
            ord(']'): self.turn_right_,
            ord('^'): self.go_north_,
            ord('_'): self.east_west_if_,
            ord('`'): self.greater_than_,
            ord('a'): self.push_ten_,
            ord('b'): self.push_eleven_,
            ord('c'): self.push_twelve_,
            ord('d'): self.push_thirteen_,
            ord('e'): self.push_fourteen_,
            ord('f'): self.push_fifteen_,
            ord('g'): self.get_,
            ord('h'): self.go_high_,
            ord('i'): self.input_file_,
            ord('j'): self.jump_forward_,
            ord('k'): self.iterate_,
            ord('l'): self.go_low_,
            ord('m'): self.high_low_if_,
            ord('n'): self.clear_stack_,
            ord('o'): self.output_file_,
            ord('p'): self.put_,
            ord('q'): self.quit_,
            ord('r'): self.reflect_,
            ord('s'): self.store_character_,
            ord('t'): self.split_,
            ord('u'): self.stack_under_stack_,
            ord('v'): self.go_south_,
            ord('w'): self.compare_,
            ord('x'): self.absolute_delta_,
            ord('y'): self.get_sysinfo_,
            ord('z'): self.no_operation_,
            ord('{'): self.begin_block_,
            ord('|'): self.north_south_if_,
            ord('}'): self.end_block_,
            ord('~'): self.input_character_,
        }

    def perform(self, ins, ip, fs):
        if ip.stringmode:
            if ins != ord('"'):
                ip.stack.push(ins)
                return InstructionResult.NONE, None

        f = self.mapping.get(ins)
        if f is not None:
            return f(ins, ip, fs)
        else:
            ip.reverse()
            return InstructionResult.NONE, None

    def empty_(self, ins, ip, fs):
        return InstructionResult.FIND, None

    def logical_not_(self, ins, ip, fs):
        v = ip.stack.pop()
        ip.stack.push(1 if v == 0 else 0)
        return InstructionResult.NONE, None

    def toggle_stringmode_(self, ins, ip, fs):
        ip.stringmode = not ip.stringmode
        return InstructionResult.NONE, None

    def trampoline_(self, ins, ip, fs):
        ip.step(fs)
        return InstructionResult.NONE, None

    def pop_(self, ins, ip, fs):
        ip.stack.pop()
        return InstructionResult.NONE, None

    def remainder_(self, ins, ip, fs):
        b = ip.stack.pop()
        a = ip.stack.pop()
        ip.stack.push(0 if b == 0 else a % b)
        return InstructionResult.NONE, None

    def input_integer_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def fetch_character_(self, ins, ip, fs):
        ip.step(fs)
        ip.stack.push(fs.get(*ip.pos))
        return InstructionResult.NONE, None

    def load_semantics_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def unload_semantics_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def multiply_(self, ins, ip, fs):
        b = ip.stack.pop()
        a = ip.stack.pop()
        ip.stack.push(a * b)
        return InstructionResult.NONE, None

    def add_(self, ins, ip, fs):
        b = ip.stack.pop()
        a = ip.stack.pop()
        ip.stack.push(a + b)
        return InstructionResult.NONE, None

    def output_character_(self, ins, ip, fs):
        v = ip.stack.pop()
        print(chr(v), end='')
        return InstructionResult.NONE, None

    def subtract_(self, ins, ip, fs):
        b = ip.stack.pop()
        a = ip.stack.pop()
        ip.stack.push(a - b)
        return InstructionResult.NONE, None

    def output_integer_(self, ins, ip, fs):
        v = ip.stack.pop()
        print(f"{v} ", end='')
        return InstructionResult.NONE, None

    def divide_(self, ins, ip, fs):
        b = ip.stack.pop()
        a = ip.stack.pop()
        ip.stack.push(0 if b == 0 else a // b)
        return InstructionResult.NONE, None

    def push_zero_(self, ins, ip, fs):
        ip.stack.push(0)
        return InstructionResult.NONE, None

    def push_one_(self, ins, ip, fs):
        ip.stack.push(1)
        return InstructionResult.NONE, None

    def push_two_(self, ins, ip, fs):
        ip.stack.push(2)
        return InstructionResult.NONE, None

    def push_three_(self, ins, ip, fs):
        ip.stack.push(3)
        return InstructionResult.NONE, None

    def push_four_(self, ins, ip, fs):
        ip.stack.push(4)
        return InstructionResult.NONE, None

    def push_five_(self, ins, ip, fs):
        ip.stack.push(5)
        return InstructionResult.NONE, None

    def push_six_(self, ins, ip, fs):
        ip.stack.push(6)
        return InstructionResult.NONE, None

    def push_seven_(self, ins, ip, fs):
        ip.stack.push(7)
        return InstructionResult.NONE, None

    def push_eight_(self, ins, ip, fs):
        ip.stack.push(8)
        return InstructionResult.NONE, None

    def push_niner_(self, ins, ip, fs):
        ip.stack.push(9)
        return InstructionResult.NONE, None

    def duplicate_(self, ins, ip, fs):
        ip.stack.duplicate()
        return InstructionResult.NONE, None

    def jump_over_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def go_west_(self, ins, ip, fs):
        ip.go_west()
        return InstructionResult.NONE, None

    def execute_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def go_east_(self, ins, ip, fs):
        ip.go_east()
        return InstructionResult.NONE, None

    def go_away_(self, ins, ip, fs):
        ip.go_away()
        return InstructionResult.NONE, None

    def stop_(self, ins, ip, fs):
        ip.alive = False
        return InstructionResult.KILL, None

    def fingerprint_defined_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def turn_left_(self, ins, ip, fs):
        ip.turn_left()
        return InstructionResult.NONE, None

    def swap_(self, ins, ip, fs):
        ip.stack.swap()
        return InstructionResult.NONE, None

    def turn_right_(self, ins, ip, fs):
        ip.turn_right()
        return InstructionResult.NONE, None

    def go_north_(self, ins, ip, fs):
        ip.go_north()
        return InstructionResult.NONE, None

    def east_west_if_(self, ins, ip, fs):
        v = ip.stack.pop()
        if v == 0:
            self.go_east_(None, ip, fs)
        else:
            self.go_west_(None, ip, fs)
        return InstructionResult.NONE, None

    def greater_than_(self, ins, ip, fs):
        b = ip.stack.pop()
        a = ip.stack.pop()
        ip.stack.push(1 if a > b else 0)
        return InstructionResult.NONE, None

    def push_ten_(self, ins, ip, fs):
        ip.stack.push(10)
        return InstructionResult.NONE, None

    def push_eleven_(self, ins, ip, fs):
        ip.stack.push(11)
        return InstructionResult.NONE, None

    def push_twelve_(self, ins, ip, fs):
        ip.stack.push(12)
        return InstructionResult.NONE, None

    def push_thirteen_(self, ins, ip, fs):
        ip.stack.push(13)
        return InstructionResult.NONE, None

    def push_fourteen_(self, ins, ip, fs):
        ip.stack.push(14)
        return InstructionResult.NONE, None

    def push_fifteen_(self, ins, ip, fs):
        ip.stack.push(15)
        return InstructionResult.NONE, None

    def get_(self, ins, ip, fs):
        r = ip.stack.pop()
        c = ip.stack.pop()
        v = fs.get(r + ip.storage_offset[0], c + ip.storage_offset[1])
        ip.stack.push(v)
        return InstructionResult.NONE, None

    def go_high_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def input_file_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def jump_forward_(self, ins, ip, fs):
        n = ip.stack.pop()
        ip.save_delta()
        if n < 0:
            ip.reverse()
            n = abs(n)
        for _ in range(n):
            ip.step(fs)
        ip.restore_delta()
        return InstructionResult.NONE, None

    def iterate_(self, ins, ip, fs):
        n = ip.stack.pop()
        ip.save_pos()
        ip.move(ins, fs)
        if n == 0:  # Just skip
            return InstructionResult.NONE, None
        ins = fs.get(*ip.pos)
        ip.restore_pos()
        res = [self.perform(ins, ip, fs) for _ in range(n)]
        return InstructionResult.ITER, res

    def go_low_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def high_low_if_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def clear_stack_(self, ins, ip, fs):
        ip.stack.clear()
        return InstructionResult.NONE, None

    def output_file_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def put_(self, ins, ip, fs):
        r = ip.stack.pop()
        c = ip.stack.pop()
        v = ip.stack.pop()
        fs.put(r + ip.storage_offset[0], c + ip.storage_offset[1], v)
        return InstructionResult.NONE, None

    def quit_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def reflect_(self, ins, ip, fs):
        ip.reverse()
        return InstructionResult.NONE, None

    def store_character_(self, ins, ip, fs):
        c = ip.stack.pop()
        ip.step(fs)
        fs.put(*ip.pos, c)
        return InstructionResult.NONE, None

    def split_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def stack_under_stack_(self, ins, ip, fs):
        ip.stack_under_stack()
        return InstructionResult.NONE, None

    def go_south_(self, ins, ip, fs):
        ip.go_south()
        return InstructionResult.NONE, None

    def compare_(self, ins, ip, fs):
        b = ip.stack.pop()
        a = ip.stack.pop()
        if a > b:
            self.turn_right_(None, ip, fs)
        elif b > a:
            self.turn_left_(None, ip, fs)
        return InstructionResult.NONE, None

    def absolute_delta_(self, ins, ip, fs):
        r = ip.stack.pop()
        c = ip.stack.pop()
        ip.absolute_vector([r, c])
        return InstructionResult.NONE, None

    def get_sysinfo_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None

    def no_operation_(self, ins, ip, fs):
        return InstructionResult.NONE, None

    def begin_block_(self, ins, ip, fs):
        ip.begin_block()
        return InstructionResult.NONE, None

    def north_south_if_(self, ins, ip, fs):
        v = ip.stack.pop()
        if v == 0:
            self.go_south_(None, ip, fs)
        else:
            self.go_north_(None, ip, fs)
        return InstructionResult.NONE, None

    def end_block_(self, ins, ip, fs):
        ip.end_block()
        return InstructionResult.NONE, None

    def input_character_(self, ins, ip, fs):
        ip.reverse()  # TODO
        return InstructionResult.NONE, None
