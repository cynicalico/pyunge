import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLabel, QSizePolicy, QFileDialog, QHBoxLayout, QFrame


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.mono_font = QFont('Source Code Pro', 12)

        self.setWindowTitle("pyunge")
        # self.setFixedSize(QSize(500, 500))

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        load = QPushButton('Load program')
        load.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addWidget(load)

        frame = QFrame()
        frame.setStyleSheet(' border: 2px solid black')
        frame.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        grid = QGridLayout()
        grid.setSpacing(1)
        grid.setContentsMargins(1, 1, 1, 1)

        for r in range(25):
            for c in range(80):
                l = QLabel('M')
                l.setFont(self.mono_font)
                l.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
                l.setStyleSheet('background-color: lightgray; padding: 0px; margin: 0px; border: none')
                grid.addWidget(l, r, c)

        frame.setLayout(grid)
        layout.addWidget(frame)

        widget = QWidget(self)
        widget.setLayout(layout)
        # widget.setStyleSheet('background-color: green')

        self.setCentralWidget(widget)

    def the_button_was_clicked(self):
        print('Clicked!')


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()


# import pyunge
# from pyunge.engine.utils import SwapList


# def main():
#     fs = pyunge.Fungespace('mycology.b98')
#
#     ips = SwapList()
#     ips.active_list().append(pyunge.InstructionPointer())
#
#     tick = 0
#     while len(ips) > 0:
#         ips.inactive_list().clear()
#         # Process each IP sequentially
#         for ip in ips.active_list():
#             while True:
#                 ins = fs.get(*ip.pos)
#                 if not ip.stringmode and (ins == ord(' ') or ins == ord(';')):
#                     ip.move(None, fs, ins == ord(';'))
#                     continue
#                 break
#             ip.cache_ins = ins
#             res, params = ip.instruction_mapping.perform(ip.cache_ins, ip, fs)
#
#             if res is pyunge.InstructionResult.MOVE:
#                 ips.inactive_list().append(ip)
#
#             elif res is pyunge.InstructionResult.SPLIT:
#                 new_ip = ip.make_copy()
#                 new_ip.reverse()
#
#                 ips.inactive_list().append(new_ip)
#                 ips.inactive_list().append(ip)
#
#             elif res is pyunge.InstructionResult.ITER:
#                 if not ip.alive:
#                     continue
#
#                 for sub_res, sub_params in params:
#                     if sub_res is pyunge.InstructionResult.SPLIT:
#                         new_ip = ip.make_copy()
#                         new_ip.reverse()
#
#                         ips.inactive_list().append(new_ip)
#
#                     if sub_res is pyunge.InstructionResult.QUIT:
#                         sys.exit(sub_params)
#
#                 ips.inactive_list().append(ip)
#
#             elif res is pyunge.InstructionResult.KILL:
#                 pass  # do nothing
#
#             elif res is pyunge.InstructionResult.QUIT:
#                 sys.exit(params)
#
#         ips.swap_active()
#         # Now move each IP if it's still alive
#         for ip in ips.active_list():
#             ip.move(ip.cache_ins, fs)
#
#         tick += 1


if __name__ == "__main__":
    main()
