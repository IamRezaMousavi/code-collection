# @Author: S.Reza Mousavi
# @Date:   2022-01-06 05:23:15
# @Last Modified by:   S.Reza Mousavi
# @Last Modified time: 2022-01-06 05:40:32


import sys

from BlurWindow.blurWindow import blur
from PyQt5 import QtCore, QtWidgets


class main(QtWidgets.QDialog):
    def __init__(self):
        super(main, self).__init__()
        self.setMinimumSize(800, 500)
        '''
        self.setWindowFlags(
            self.windowFlags() | QtCore.Qt.FramelessWindowHint
        )
        '''
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, on=True)

        hwnd = self.winId()
        blur(hwnd)

        self.setStyleSheet('background-color: rgba(0, 0, 0, 0)')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mw = main()
    mw.setWindowOpacity(0.80)
    mw.show()
    sys.exit(app.exec())
