import pyunge


def main():
    fs = pyunge.Fungespace()
    fs.set(1, 1, 'A')
    fs.set(1, -1, 'A')
    fs.set(-1, 1, 'A')
    fs.set(-1, -1, 'A')
    fs.set(-1, -5, 'B')

    print(fs, end='')


if __name__ == "__main__":
    main()
