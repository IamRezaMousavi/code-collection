# -*- coding: utf-8 -*-
# @Author: @IamRezaMousavi
# @Date:   2022-03-18 23:03:09
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-04-28 02:41:25

from datetime import datetime
from time import sleep
import sys

from PIL import ImageGrab
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        saveButton = QPushButton("Take Screenshot", self)
        saveButton.clicked.connect(self.takeScreenshot)
    
    def takeScreenshot(self):
        
        self.showMinimized()
        sleep(0.4)
    
        fileName = "Screenshot-" + datetime.strftime(datetime.now(), "%Y.%m.%d-%H.%M.%S")
        
        screenshot = ImageGrab.grab()
        screenshot.save(fileName + ".png", "PNG")
        
        self.showNormal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
