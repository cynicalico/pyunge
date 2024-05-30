import datetime
import math
import os

from pyunge.engine.instruction_result import InstructionResult


def logical_not(instruction_mapping, ins, ip, fs):
    v = ip.stack.pop()
    ip.stack.push(1 if v == 0 else 0)
    return InstructionResult.NONE, None


def toggle_stringmode(instruction_mapping, ins, ip, fs):
    ip.stringmode = not ip.stringmode
    return InstructionResult.NONE, None


def trampoline(instruction_mapping, ins, ip, fs):
    ip.step(fs)
    return InstructionResult.NONE, None


def pop(instruction_mapping, ins, ip, fs):
    ip.stack.pop()
    return InstructionResult.NONE, None


def remainder(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(0 if b == 0 else a % b)
    return InstructionResult.NONE, None


def input_integer(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def fetch_character(instruction_mapping, ins, ip, fs):
    ip.step(fs)
    ip.stack.push(fs.get(*ip.pos))
    return InstructionResult.NONE, None


def load_semantics(instruction_mapping, ins, ip, fs):
    n = ip.stack.pop()
    fingerprint = 0
    for _ in range(n):
        fingerprint *= 256
        fingerprint + ip.stack.pop()
    ip.reverse()
    return InstructionResult.NONE, None


def unload_semantics(instruction_mapping, ins, ip, fs):
    n = ip.stack.pop()
    fingerprint = 0
    for _ in range(n):
        fingerprint *= 256
        fingerprint + ip.stack.pop()
    ip.reverse()
    return InstructionResult.NONE, None


def multiply(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(a * b)
    return InstructionResult.NONE, None


def add(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(a + b)
    return InstructionResult.NONE, None


def output_character(instruction_mapping, ins, ip, fs):
    v = ip.stack.pop()
    print(chr(v), end='')
    return InstructionResult.NONE, None


def subtract(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(a - b)
    return InstructionResult.NONE, None


def output_integer(instruction_mapping, ins, ip, fs):
    v = ip.stack.pop()
    print(f"{v} ", end='')
    return InstructionResult.NONE, None


def divide(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(0 if b == 0 else a // b)
    return InstructionResult.NONE, None


def push_zero(instruction_mapping, ins, ip, fs):
    ip.stack.push(0)
    return InstructionResult.NONE, None


def push_one(instruction_mapping, ins, ip, fs):
    ip.stack.push(1)
    return InstructionResult.NONE, None


def push_two(instruction_mapping, ins, ip, fs):
    ip.stack.push(2)
    return InstructionResult.NONE, None


def push_three(instruction_mapping, ins, ip, fs):
    ip.stack.push(3)
    return InstructionResult.NONE, None


def push_four(instruction_mapping, ins, ip, fs):
    ip.stack.push(4)
    return InstructionResult.NONE, None


def push_five(instruction_mapping, ins, ip, fs):
    ip.stack.push(5)
    return InstructionResult.NONE, None


def push_six(instruction_mapping, ins, ip, fs):
    ip.stack.push(6)
    return InstructionResult.NONE, None


def push_seven(instruction_mapping, ins, ip, fs):
    ip.stack.push(7)
    return InstructionResult.NONE, None


def push_eight(instruction_mapping, ins, ip, fs):
    ip.stack.push(8)
    return InstructionResult.NONE, None


def push_niner(instruction_mapping, ins, ip, fs):
    ip.stack.push(9)
    return InstructionResult.NONE, None


def duplicate(instruction_mapping, ins, ip, fs):
    ip.stack.duplicate()
    return InstructionResult.NONE, None


def go_west(instruction_mapping, ins, ip, fs):
    ip.go_west()
    return InstructionResult.NONE, None


def execute(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def go_east(instruction_mapping, ins, ip, fs):
    ip.go_east()
    return InstructionResult.NONE, None


def go_away(instruction_mapping, ins, ip, fs):
    ip.go_away()
    return InstructionResult.NONE, None


def stop(instruction_mapping, ins, ip, fs):
    ip.alive = False
    return InstructionResult.KILL, None


def fingerprint_defined(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def turn_left(instruction_mapping, ins, ip, fs):
    ip.turn_left()
    return InstructionResult.NONE, None


def swap(instruction_mapping, ins, ip, fs):
    ip.stack.swap()
    return InstructionResult.NONE, None


def turn_right(instruction_mapping, ins, ip, fs):
    ip.turn_right()
    return InstructionResult.NONE, None


def go_north(instruction_mapping, ins, ip, fs):
    ip.go_north()
    return InstructionResult.NONE, None


def east_west_if(instruction_mapping, ins, ip, fs):
    v = ip.stack.pop()
    if v == 0:
        go_east(instruction_mapping, None, ip, fs)
    else:
        go_west(instruction_mapping, None, ip, fs)
    return InstructionResult.NONE, None


def greater_than(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    ip.stack.push(1 if a > b else 0)
    return InstructionResult.NONE, None


def push_ten(instruction_mapping, ins, ip, fs):
    ip.stack.push(10)
    return InstructionResult.NONE, None


def push_eleven(instruction_mapping, ins, ip, fs):
    ip.stack.push(11)
    return InstructionResult.NONE, None


def push_twelve(instruction_mapping, ins, ip, fs):
    ip.stack.push(12)
    return InstructionResult.NONE, None


def push_thirteen(instruction_mapping, ins, ip, fs):
    ip.stack.push(13)
    return InstructionResult.NONE, None


def push_fourteen(instruction_mapping, ins, ip, fs):
    ip.stack.push(14)
    return InstructionResult.NONE, None


def push_fifteen(instruction_mapping, ins, ip, fs):
    ip.stack.push(15)
    return InstructionResult.NONE, None


def get(instruction_mapping, ins, ip, fs):
    r = ip.stack.pop()
    c = ip.stack.pop()
    v = fs.get(r + ip.storage_offset[0], c + ip.storage_offset[1])
    ip.stack.push(v)
    return InstructionResult.NONE, None


def go_high(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def input_file(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def jump_forward(instruction_mapping, ins, ip, fs):
    n = ip.stack.pop()
    ip.save_delta()
    if n < 0:
        ip.reverse()
        n = abs(n)
    for _ in range(n):
        ip.step(fs)
    ip.restore_delta()
    return InstructionResult.NONE, None


def iterate(instruction_mapping, ins, ip, fs):
    n = ip.stack.pop()
    ip.save_pos()
    ip.move(ins, fs)
    if n == 0:  # Just skip
        return InstructionResult.NONE, None
    ins = fs.get(*ip.pos)
    ip.restore_pos()
    res = [instruction_mapping.perform(ins, ip, fs) for _ in range(n)]
    return InstructionResult.ITER, res


def go_low(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def high_low_if(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def clear_stack(instruction_mapping, ins, ip, fs):
    ip.stack.clear()
    return InstructionResult.NONE, None


def output_file(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def put(instruction_mapping, ins, ip, fs):
    r = ip.stack.pop()
    c = ip.stack.pop()
    v = ip.stack.pop()
    fs.put(r + ip.storage_offset[0], c + ip.storage_offset[1], v)
    return InstructionResult.NONE, None


def quit(instruction_mapping, ins, ip, fs):
    n = ip.stack.pop()
    return InstructionResult.QUIT, n


def reflect(instruction_mapping, ins, ip, fs):
    ip.reverse()
    return InstructionResult.NONE, None


def store_character(instruction_mapping, ins, ip, fs):
    c = ip.stack.pop()
    ip.step(fs)
    fs.put(*ip.pos, c)
    return InstructionResult.NONE, None


def split(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None


def stack_under_stack(instruction_mapping, ins, ip, fs):
    ip.stack_under_stack()
    return InstructionResult.NONE, None


def go_south(instruction_mapping, ins, ip, fs):
    ip.go_south()
    return InstructionResult.NONE, None


def compare(instruction_mapping, ins, ip, fs):
    b = ip.stack.pop()
    a = ip.stack.pop()
    if a > b:
        turn_right(instruction_mapping, None, ip, fs)
    elif b > a:
        turn_left(instruction_mapping, None, ip, fs)
    return InstructionResult.NONE, None


def absolute_delta(instruction_mapping, ins, ip, fs):
    r = ip.stack.pop()
    c = ip.stack.pop()
    ip.absolute_vector([r, c])
    return InstructionResult.NONE, None


def get_sysinfo(instruction_mapping, ins, ip, fs):
    n = ip.stack.pop()

    sysinfo = []

    # 0x01: high if t is implemented
    # 0x02: high if i is implemented
    # 0x04: high if o is implemented
    # 0x08: high if = is implemented
    # 0x10: high if unbuffered stdio
    sysinfo.append(0b00000)

    # number of bytes per cell
    sysinfo.append(math.inf)

    # implementation's handprint
    sysinfo.append(0)

    # implementation's version number
    sysinfo.append(1)

    # id code for the operating paradigm
    # 0 = unavailable
    # 1 = equivalent to C-language `system()` call behavior
    # 2 = equivalent to interpretation by a specific shell of program (document)
    # 3 = equivalent to interpretation by the same shell that started this Funge interpreter
    sysinfo.append(0)

    # path separator character
    sysinfo.append(ord('/'))

    # number of scalars per vector (1 for une, 2 for be, 3 for trefunge)
    sysinfo.append(2)

    # unique ID for current IP
    sysinfo.append(0)

    # unique team number for current IP
    sysinfo.append(0)

    # fungespace position of current IP
    sysinfo.extend(ip.pos)

    # fungespace delta of current IP
    sysinfo.extend(ip.delta)

    # fungespace storage offset of current IP
    sysinfo.extend(ip.storage_offset)

    # TODO: This is the least point which has *ever* had a cell,
    #       but if you were to change it to space it would still
    #       think this is the minimum point
    # least point which contains a non-space cell
    sysinfo.extend(fs.min_coord)

    # TODO: See above TODO, but for greatest point instead
    # greatest point which contains a non-space cell relative to the least
    sysinfo.extend([fs.max_coord[0] + abs(fs.min_coord[0]),
                    fs.max_coord[1] + abs(fs.min_coord[1])])

    now = datetime.datetime.now()
    # current ((year - 1900) * 256 * 256) + (month * 256) + (day of month)
    sysinfo.append(((now.year - 1900) * 256 * 256) + (now.month * 256) + now.day)

    # current (hour * 256 * 256) + (minute * 256) + (second)
    sysinfo.append((now.hour * 256 * 256) + (now.minute * 256) + now.second)

    # number of stacks in use by IP
    sysinfo.append(len(ip.stack.stacks))

    # size of each stack in stackstack (from TOSS to BOSS)
    for stack in ip.stack.stacks:
        sysinfo.append(len(stack))

    # command line arguments followed by double null
    # TODO
    sysinfo.append(ord('\0'))
    sysinfo.append(ord('\0'))

    # env variables followed by null
    for k, v in os.environ.items():
        for c in k:
            sysinfo.append(ord(c))
        sysinfo.append(ord('='))
        for c in v:
            sysinfo.append(ord(c))
        sysinfo.append(ord('\0'))
    sysinfo.append(ord('\0'))

    if n <= 0:
        # add all this info to the stack (reversed, so it's in the correct order)
        ip.stack.extend_(sysinfo[::-1])

    else:
        if n <= len(sysinfo):
            ip.stack.push(sysinfo[n - 1])
        else:
            ip.stack.push(ip.stack.pick(n - len(sysinfo)))

    return InstructionResult.NONE, None


def no_operation(instruction_mapping, ins, ip, fs):
    return InstructionResult.NONE, None


def begin_block(instruction_mapping, ins, ip, fs):
    ip.begin_block()
    return InstructionResult.NONE, None


def north_south_if(instruction_mapping, ins, ip, fs):
    v = ip.stack.pop()
    if v == 0:
        go_south(instruction_mapping, None, ip, fs)
    else:
        go_north(instruction_mapping, None, ip, fs)
    return InstructionResult.NONE, None


def end_block(instruction_mapping, ins, ip, fs):
    ip.end_block()
    return InstructionResult.NONE, None


def input_character(instruction_mapping, ins, ip, fs):
    ip.reverse()  # TODO
    return InstructionResult.NONE, None
