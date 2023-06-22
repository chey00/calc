import binascii

import PyQt6
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QSlider, QHBoxLayout, QTextBrowser, QGridLayout, QLabel, QLineEdit, QTextBrowser, \
    QLCDNumber
from PyQt6.QtCore import pyqtSlot, Qt, QSize


class CentralWidget(QWidget):
    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        layout = QGridLayout(self)

        self.display = QLCDNumber(parent)

        self.bin = QLineEdit(parent)
        self.hex = QLineEdit(parent)

        self.bin.setInputMask("B" + 7 * "b")
        self.hex.setInputMask("Hh")

        self.bin.setText("0")
        self.hex.setText("0")

        self.bin.editingFinished.connect(self.calc)
        self.hex.editingFinished.connect(self.calc)

        layout.addWidget(self.display, 1, 1, 1, 2)

        layout.addWidget(QLabel("Dezimal:"), 2, 1, Qt.AlignmentFlag.AlignRight)
        layout.addWidget(QLabel("Hexadezimal:"), 3, 1, Qt.AlignmentFlag.AlignRight)

        layout.addWidget(self.bin, 2, 2)
        layout.addWidget(self.hex, 3, 2)

        self.setLayout(layout)

    @pyqtSlot()
    def calc(self):
        is_valid = True

        is_valid = is_valid and self.bin.hasAcceptableInput()
        is_valid = is_valid and self.hex.hasAcceptableInput()

        if is_valid:
            str_bin = self.bin.text()
            str_hex = self.hex.text()

            print(str_bin + str_hex)

            self.display.display(str_bin + str_hex)
        else:
            print("Input is not valid.")
