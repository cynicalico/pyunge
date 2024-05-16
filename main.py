import pyunge


def main():
    fs = pyunge.Fungespace()
    fs.set(1, 1, 'A')
    fs.set(1, -1, 'A')
    fs.set(-1, 1, 'A')
    fs.set(-1, -1, 'A')
    fs.set(-1, -5, 'B')
    print(fs, end='')

    ss = pyunge.StackStack()
    ss.extend_([1, 2, 3, 4, 5, 3])

    print(ss.stacks)
    ss.begin_block([10, 10])
    print(ss.stacks)

    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.duplicate()
    ss.push(-2)

    print(ss.stacks)
    print(ss.end_block())
    print(ss.stacks)
    print(ss.end_block())
    print(ss.stacks)

    ss.push(1)
    ss.push(2)
    ss.push(3)
    ss.push(4)
    ss.push(5)
    ss.push(0)
    print(ss.stacks)
    ss.begin_block([10, 10])
    print(ss.stacks)
    ss.push(3)
    ss.stack_under_stack()
    print(ss.stacks)


if __name__ == "__main__":
    main()
