# @Author: @IamRezaMousavi
# @Date:   2022-03-18 23:03:09
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-03-20 21:20:49

import sys

from PyQt5.QtWidgets import QApplication, QFileDialog, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        saveButton = QPushButton('SAVE', self)
        saveButton.clicked.connect(self.saveFile)

    def saveFile(self):
        name = QFileDialog.getSaveFileName(self, 'Save File', filter='Text Files (*.txt)')
        try:
            with open(name[0], 'w') as f:
                f.write('YA ALLAH')
        except FileNotFoundError:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
