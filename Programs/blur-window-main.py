# @Author: @IamRezaMousavi
# @Date:   2022-03-20 21:54:23
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-20 22:07:31

import sys

from BlurWindow.blurWindow import GlobalBlur
from PyQt5 import QtCore, QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        GlobalBlur(self.winId(), Dark=True, QWidget=self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
