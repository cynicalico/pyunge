from collections import deque

import pyunge.engine.fingerprints.MODU as MODU
import pyunge.engine.fingerprints.ROMA as ROMA
from pyunge.engine import base_instruction_set
from pyunge.engine.instruction_result import InstructionResult


class InstructionStack:
    def __init__(self, fingerprint, f):
        self.d = deque([(fingerprint, f)])

    def __call__(self, *args, **kwargs):
        return self.d[-1][1](*args, **kwargs)

    def push(self, fingerprint, f):
        self.d.append((fingerprint, f))

    def pop(self, fingerprint):
        # TODO: Is this seriously correct? Mycology seems to think so...
        self.d.pop()
        # for _ in range(len(self.d)):
        #     item = self.d.popleft()
        #     if item[0] != fingerprint:
        #         self.d.append(item)


class InstructionMapping:
    def __init__(self):
        self.mapping = {
            ord(' '): None,
            ord('!'): InstructionStack(None, base_instruction_set.logical_not),
            ord('"'): InstructionStack(None, base_instruction_set.toggle_stringmode),
            ord('#'): InstructionStack(None, base_instruction_set.trampoline),
            ord('$'): InstructionStack(None, base_instruction_set.pop),
            ord('%'): InstructionStack(None, base_instruction_set.remainder),
            ord('&'): InstructionStack(None, base_instruction_set.input_integer),
            ord('\''): InstructionStack(None, base_instruction_set.fetch_character),
            ord('('): InstructionStack(None, base_instruction_set.load_semantics),
            ord(')'): InstructionStack(None, base_instruction_set.unload_semantics),
            ord('*'): InstructionStack(None, base_instruction_set.multiply),
            ord('+'): InstructionStack(None, base_instruction_set.add),
            ord(','): InstructionStack(None, base_instruction_set.output_character),
            ord('-'): InstructionStack(None, base_instruction_set.subtract),
            ord('.'): InstructionStack(None, base_instruction_set.output_integer),
            ord('/'): InstructionStack(None, base_instruction_set.divide),
            ord('0'): InstructionStack(None, base_instruction_set.push_zero),
            ord('1'): InstructionStack(None, base_instruction_set.push_one),
            ord('2'): InstructionStack(None, base_instruction_set.push_two),
            ord('3'): InstructionStack(None, base_instruction_set.push_three),
            ord('4'): InstructionStack(None, base_instruction_set.push_four),
            ord('5'): InstructionStack(None, base_instruction_set.push_five),
            ord('6'): InstructionStack(None, base_instruction_set.push_six),
            ord('7'): InstructionStack(None, base_instruction_set.push_seven),
            ord('8'): InstructionStack(None, base_instruction_set.push_eight),
            ord('9'): InstructionStack(None, base_instruction_set.push_niner),
            ord(':'): InstructionStack(None, base_instruction_set.duplicate),
            ord(';'): None,
            ord('<'): InstructionStack(None, base_instruction_set.go_west),
            ord('='): InstructionStack(None, base_instruction_set.execute),
            ord('>'): InstructionStack(None, base_instruction_set.go_east),
            ord('?'): InstructionStack(None, base_instruction_set.go_away),
            ord('@'): InstructionStack(None, base_instruction_set.stop),
            ord('A'): InstructionStack(None, base_instruction_set.reflect),
            ord('B'): InstructionStack(None, base_instruction_set.reflect),
            ord('C'): InstructionStack(None, base_instruction_set.reflect),
            ord('D'): InstructionStack(None, base_instruction_set.reflect),
            ord('E'): InstructionStack(None, base_instruction_set.reflect),
            ord('F'): InstructionStack(None, base_instruction_set.reflect),
            ord('G'): InstructionStack(None, base_instruction_set.reflect),
            ord('H'): InstructionStack(None, base_instruction_set.reflect),
            ord('I'): InstructionStack(None, base_instruction_set.reflect),
            ord('J'): InstructionStack(None, base_instruction_set.reflect),
            ord('K'): InstructionStack(None, base_instruction_set.reflect),
            ord('L'): InstructionStack(None, base_instruction_set.reflect),
            ord('M'): InstructionStack(None, base_instruction_set.reflect),
            ord('N'): InstructionStack(None, base_instruction_set.reflect),
            ord('O'): InstructionStack(None, base_instruction_set.reflect),
            ord('P'): InstructionStack(None, base_instruction_set.reflect),
            ord('Q'): InstructionStack(None, base_instruction_set.reflect),
            ord('R'): InstructionStack(None, base_instruction_set.reflect),
            ord('S'): InstructionStack(None, base_instruction_set.reflect),
            ord('T'): InstructionStack(None, base_instruction_set.reflect),
            ord('U'): InstructionStack(None, base_instruction_set.reflect),
            ord('V'): InstructionStack(None, base_instruction_set.reflect),
            ord('W'): InstructionStack(None, base_instruction_set.reflect),
            ord('X'): InstructionStack(None, base_instruction_set.reflect),
            ord('Y'): InstructionStack(None, base_instruction_set.reflect),
            ord('Z'): InstructionStack(None, base_instruction_set.reflect),
            ord('['): InstructionStack(None, base_instruction_set.turn_left),
            ord('\\'): InstructionStack(None, base_instruction_set.swap),
            ord(']'): InstructionStack(None, base_instruction_set.turn_right),
            ord('^'): InstructionStack(None, base_instruction_set.go_north),
            ord('_'): InstructionStack(None, base_instruction_set.east_west_if),
            ord('`'): InstructionStack(None, base_instruction_set.greater_than),
            ord('a'): InstructionStack(None, base_instruction_set.push_ten),
            ord('b'): InstructionStack(None, base_instruction_set.push_eleven),
            ord('c'): InstructionStack(None, base_instruction_set.push_twelve),
            ord('d'): InstructionStack(None, base_instruction_set.push_thirteen),
            ord('e'): InstructionStack(None, base_instruction_set.push_fourteen),
            ord('f'): InstructionStack(None, base_instruction_set.push_fifteen),
            ord('g'): InstructionStack(None, base_instruction_set.get),
            ord('h'): InstructionStack(None, base_instruction_set.go_high),
            ord('i'): InstructionStack(None, base_instruction_set.input_file),
            ord('j'): InstructionStack(None, base_instruction_set.jump_forward),
            ord('k'): InstructionStack(None, base_instruction_set.iterate),
            ord('l'): InstructionStack(None, base_instruction_set.go_low),
            ord('m'): InstructionStack(None, base_instruction_set.high_low_if),
            ord('n'): InstructionStack(None, base_instruction_set.clear_stack),
            ord('o'): InstructionStack(None, base_instruction_set.output_file),
            ord('p'): InstructionStack(None, base_instruction_set.put),
            ord('q'): InstructionStack(None, base_instruction_set.quit),
            ord('r'): InstructionStack(None, base_instruction_set.reflect),
            ord('s'): InstructionStack(None, base_instruction_set.store_character),
            ord('t'): InstructionStack(None, base_instruction_set.split),
            ord('u'): InstructionStack(None, base_instruction_set.stack_under_stack),
            ord('v'): InstructionStack(None, base_instruction_set.go_south),
            ord('w'): InstructionStack(None, base_instruction_set.compare),
            ord('x'): InstructionStack(None, base_instruction_set.absolute_delta),
            ord('y'): InstructionStack(None, base_instruction_set.get_sysinfo),
            ord('z'): InstructionStack(None, base_instruction_set.no_operation),
            ord('{'): InstructionStack(None, base_instruction_set.begin_block),
            ord('|'): InstructionStack(None, base_instruction_set.north_south_if),
            ord('}'): InstructionStack(None, base_instruction_set.end_block),
            ord('~'): InstructionStack(None, base_instruction_set.input_character),
        }

        self.known_fingerprints = {
            MODU.ID: MODU.MAPPING,
            ROMA.ID: ROMA.MAPPING
        }

    def perform(self, ins, ip, fs):
        if ip.stringmode:
            if ins != ord('"'):
                ip.stack.push(ins)
                return InstructionResult.MOVE, None

        f = self.mapping.get(ins)
        if f is not None:
            return f(self, ins, ip, fs)
        else:
            ip.reverse()
            return InstructionResult.MOVE, None

    def load_fingerprint(self, ins, ip, fs, fingerprint):
        fingerprint_mapping = self.known_fingerprints.get(fingerprint)
        if fingerprint_mapping is not None:
            for mapped_ins, f in fingerprint_mapping.items():
                ins_stack = self.mapping.get(mapped_ins)
                if ins_stack is not None:
                    ins_stack.push(fingerprint, f)
            return True
        return False

    def unload_fingerprint(self, ins, ip, fs, fingerprint):
        fingerprint_mapping = self.known_fingerprints.get(fingerprint)
        if fingerprint_mapping is not None:
            for mapped_ins, _ in fingerprint_mapping.items():
                ins_stack = self.mapping.get(mapped_ins)
                if ins_stack is not None:
                    ins_stack.pop(fingerprint)
            return True
        return False
