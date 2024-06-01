import sys
from collections import deque

import pyunge
from pyunge.engine.utils import SwapList


# import colorama
# from colorama import Fore, Style
#
# TICK_OF_INTEREST = None
# INTEREST_ZONE_BUFFER = 100
# INTEREST_ZONE_SIZE = 100
#
# if TICK_OF_INTEREST is not None:
#     if TICK_OF_INTEREST - INTEREST_ZONE_BUFFER <= tick <= TICK_OF_INTEREST + INTEREST_ZONE_BUFFER:
#         fs_width = (fs.max_coord[1] - fs.min_coord[1] + 1)
#
#         ts = f"TICK {tick}"
#         l1 = (fs_width - len(ts)) // 2
#         l2 = (fs_width - len(ts)) - l1
#         print(f"{'-' * l1}{ts}{'-' * l2}")
#
#         for ip in ips:
#             for r in range(ip.pos[0] - INTEREST_ZONE_SIZE, ip.pos[0] + INTEREST_ZONE_SIZE):
#                 if r < fs.min_coord[0]:
#                     continue
#                 if r > fs.max_coord[0]:
#                     break
#                 s = ''
#                 for c in range(fs.min_coord[1], fs.max_coord[1] + 1):
#                     v = fs.get(r, c)
#                     ch = chr(v) if v != ord(' ') else '☐'
#                     if r == ip.pos[0] and c == ip.pos[1]:
#                         if ip.id == 1:
#                             s += f"{Fore.LIGHTGREEN_EX}{ch}{Style.RESET_ALL}"
#                         else:
#                             s += f"{Fore.LIGHTRED_EX}{ch}{Style.RESET_ALL}"
#                     else:
#                         if ch == '☐':
#                             s += f"{Fore.LIGHTBLACK_EX}{ch}{Style.RESET_ALL}"
#                         else:
#                             s += f"{ch}"
#                 print(s)
#             print('-' * fs_width)
#
#         print()


def main():
    fs = pyunge.Fungespace('programs/mycology.b98')

    ips = SwapList()
    ips.active_list().append(pyunge.InstructionPointer())

    tick = 0
    while len(ips) > 0:
        # Make sure each IP is on a valid cell
        for ip in ips.active_list():
            while True:
                ins = fs.get(*ip.pos)
                if not ip.stringmode and (ins == ord(' ') or ins == ord(';')):
                    ip.move(None, fs)
                    continue
                break

        ips.inactive_list().clear()
        # Process each IP sequentially
        for ip in ips.active_list():
            ins = fs.get(*ip.pos)
            ip.cache_ins = ins
            res, params = ip.instruction_mapping.perform(ip.cache_ins, ip, fs)

            if res is pyunge.InstructionResult.MOVE:
                ips.inactive_list().append(ip)

            elif res is pyunge.InstructionResult.SPLIT:
                new_ip = ip.make_copy()
                new_ip.reverse()

                ips.inactive_list().append(new_ip)
                ips.inactive_list().append(ip)

            elif res is pyunge.InstructionResult.ITER:
                if not ip.alive:
                    continue

                should_split = False
                for sub_res, sub_params in params:
                    if sub_res is pyunge.InstructionResult.SPLIT:
                        should_split = True

                    if sub_res is pyunge.InstructionResult.QUIT:
                        sys.exit(sub_params)

                if should_split:
                    new_ip = ip.make_copy()
                    new_ip.reverse()

                    ips.inactive_list().append(new_ip)
                ips.inactive_list().append(ip)

            elif res is pyunge.InstructionResult.KILL:
                pass  # do nothing

            elif res is pyunge.InstructionResult.QUIT:
                sys.exit(params)

        ips.swap_active()
        # Now move each IP if it's still alive
        for ip in ips.active_list():
            ip.move(ip.cache_ins, fs)

        tick += 1


if __name__ == "__main__":
    main()
