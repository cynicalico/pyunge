import enum


# Instruction functions will have the following signature:
# def i(instruction_mapping, ins, ip, fs)


class InstructionResult(enum.Enum):
    NONE = enum.auto()
    # params: None

    KILL = enum.auto()
    # params: None

    SPLIT = enum.auto()
    # params: None

    QUIT = enum.auto()
    # params: code - exit code for sys.exit

    ITER = enum.auto()
    # params: res - list of InstructionResult/param pairs
