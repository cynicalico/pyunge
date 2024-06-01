from pyunge.engine.instruction_result import InstructionResult


def roma_c(instruction_mapping, ins, ip, fs):
    ip.stack.push(100)
    return InstructionResult.MOVE, None


def roma_d(instruction_mapping, ins, ip, fs):
    ip.stack.push(500)
    return InstructionResult.MOVE, None


def roma_i(instruction_mapping, ins, ip, fs):
    ip.stack.push(1)
    return InstructionResult.MOVE, None


def roma_l(instruction_mapping, ins, ip, fs):
    ip.stack.push(50)
    return InstructionResult.MOVE, None


def roma_m(instruction_mapping, ins, ip, fs):
    ip.stack.push(1000)
    return InstructionResult.MOVE, None


def roma_v(instruction_mapping, ins, ip, fs):
    ip.stack.push(5)
    return InstructionResult.MOVE, None


def roma_x(instruction_mapping, ins, ip, fs):
    ip.stack.push(10)
    return InstructionResult.MOVE, None


ID = 0x524f4d41
MAPPING = {
    ord('C'): roma_c,
    ord('D'): roma_d,
    ord('I'): roma_i,
    ord('L'): roma_l,
    ord('M'): roma_m,
    ord('V'): roma_v,
    ord('X'): roma_x
}
