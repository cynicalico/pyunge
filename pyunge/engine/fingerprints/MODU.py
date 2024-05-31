from pyunge.engine.instruction_result import InstructionResult
import math


def modu_m(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(0 if b == 0 else a % b)
    return InstructionResult.NONE, None


def modu_u(instruction_mapping, ins, ip, fs):
    # FIXME: I can't find any info on what "Sam Holden's Unsigned Modulo" is, but this
    #        does give the correct answer for the single Mycology test case
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(0 if b == 0 else abs(a) % abs(b))
    return InstructionResult.NONE, None


def modu_r(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(0 if b == 0 else math.remainder(a, b))
    return InstructionResult.NONE, None


ID = 0x4d4f4455
MAPPING = {
    ord('M'): modu_m,
    ord('U'): modu_u,
    ord('R'): modu_r,
}
