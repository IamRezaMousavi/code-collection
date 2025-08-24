# @Author: @IamRezaMousavi
# @Date:   2022-02-12 12:31:32
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-02-12 12:42:30

import sys

from PyQt5 import QtGui, QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    trayIcon = QtWidgets.QSystemTrayIcon(QtGui.QIcon('QSystemTrayIcon.png'), w)
    menu = QtWidgets.QMenu(w)
    exitAction = menu.addAction('Exit')
    exitAction.triggered.connect(app.quit)
    trayIcon.setContextMenu(menu)

    trayIcon.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
