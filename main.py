import sys

import pyunge


def main():
    fs = pyunge.Fungespace('programs/mycology.b98')
    ips = [pyunge.InstructionPointer()]

    while any(ip.alive for ip in ips):
        ips = list(filter(lambda ip: ip.alive, ips))
        for ip in ips:
            ins = fs.get(*ip.pos)

            res, params = ip.instruction_mapping.perform(ins, ip, fs)
            # print(f"ins: {ins} '{chr(ins)}', res: {res}, params: {params}")

            if res is pyunge.InstructionResult.KILL:
                continue

            elif res is pyunge.InstructionResult.QUIT:
                sys.exit(params)

            ip.move(ins, fs)


if __name__ == "__main__":
    main()
