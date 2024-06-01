import math

from pyunge.engine.instruction_result import InstructionResult


def modu_m(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(0 if b == 0 else a % b)
    return InstructionResult.MOVE, None


def modu_u(instruction_mapping, ins, ip, fs):
    # This is what rcfunge does, possibly should be math.remainder(a, b)
    # but without more test programs that actually use it, who knows
    b = abs(ip.stack.pop())
    a = abs(ip.stack.pop())
    ip.stack.push(0 if b == 0 else a % b)
    return InstructionResult.MOVE, None


def modu_r(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(0 if b == 0 else math.remainder(a, b))
    return InstructionResult.MOVE, None


ID = 0x4d4f4455
MAPPING = {
    ord('M'): modu_m,
    ord('U'): modu_u,
    ord('R'): modu_r,
}
