# @Author: @IamRezaMousavi
# @Date:   2022-01-17 20:00:37
# @Last Modified by:   @IamRezaMousavi
# @Last Modified time: 2022-09-25 11:11:08

import sys
from math import pow, sqrt

import pyqtgraph as pg
from communication import Communication
from dataBase import DataBase
from PyQt5.QtCore import QPoint, Qt, QTimer
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QDesktopWidget,
    QGridLayout,
    QGroupBox,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
)
from serial.tools import list_ports


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.setWindowTitle('Flight Monitoring')
        self.setMinimumSize(1000, 580)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ser = Communication()
        self.dataBase = DataBase()

        self.combobox = QComboBox()
        portsList = [str(comport) for comport in list_ports.comports()]
        self.combobox.addItems(sorted(portsList))
        self.combobox.setStyleSheet(
            """QComboBox
                {
                    background: transparent;
                    color: white;
                    border: 1px solid white;
                    border-radius: 5px;
                    padding: 1px 25px;
                }
                QComboBox QAbstractItemView
                {
                    background: transparent;
                    color: white;
                    selection-background-color: darkblue;
                    border: 1px solid white;
                    border-radius: 5px;
                }
            """,
        )

        startButton = QPushButton('Start')
        startButton.clicked.connect(self.startPloting)
        startButton.setStyleSheet(
            """QPushButton
                                 {
                                     background: transparent;
                                     color: rgb(0, 150, 0);
                                     border: 1px solid;
                                     border-radius: 5px;
                                     border-color: green;
                                     font: 16px;
                                 }
                                 QPushButton:pressed
                                 {
                                     background: rgb(0, 150, 0);
                                     color: black;
                                 }
                                 """,
        )
        stopButton = QPushButton('Stop')
        stopButton.clicked.connect(self.stopPloting)
        stopButton.setStyleSheet(
            """QPushButton
                                 {
                                     background: transparent;
                                     color: blue;
                                     border: 1px solid;
                                     border-radius: 5px;
                                     border-color: blue;
                                     font: 16px;
                                 }
                                 QPushButton:pressed
                                 {
                                     background: blue;
                                     color: black;
                                 }
                                 """,
        )
        clearButton = QPushButton('Clear')
        clearButton.clicked.connect(self.clearPloting)
        clearButton.setStyleSheet(
            """QPushButton
                                 {
                                     background: transparent;
                                     color: yellow;
                                     border: 1px solid;
                                     border-radius: 5px;
                                     border-color: yellow;
                                     font: 16px;
                                 }
                                 QPushButton:pressed
                                 {
                                     background-color: yellow;
                                     color: black;
                                 }
                                 """,
        )
        exitButton = QPushButton('X')
        exitButton.clicked.connect(app.exit)
        exitButton.setStyleSheet(
            """QPushButton
                                 {
                                     background: transparent;
                                     color: red;
                                     border: 1px solid;
                                     border-radius: 2px;
                                     border-color: red;
                                     font: bold 10px;
                                     padding: 5px 5px;
                                 }
                                 QPushButton:pressed
                                 {
                                     background: red;
                                     color: black;
                                 }
                                 """,
        )

        graphWidget = pg.PlotWidget(title='Altitude (m)', background='#0f0f0f')
        self.xValues = list(range(30))
        self.yValues = [0] * 30
        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = graphWidget.plot(self.xValues, self.yValues, pen=pen)
        graphWidget.showGrid(x=True, y=True)

        speedGraph = pg.PlotWidget(title='Speed (m/s)', background='#0f0f0f')
        self.speedData = [0] * 20
        self.speedGraphLine = speedGraph.plot(self.speedData, pen=pen)
        speedGraph.showGrid(x=True, y=True)
        self.vx = self.vy = self.vz = self.speedGraphPtr = 0

        accGraph = pg.PlotWidget(title='Accelerations (m/s²)', background='#0f0f0f')
        accGraph.addLegend()
        accGraph.hideAxis('bottom')
        self.accX = [0] * 30
        self.accY = [0] * 30
        self.accZ = [0] * 30
        self.AccXLine = accGraph.plot(self.accX, pen=(102, 252, 241), name='X')
        self.AccYLine = accGraph.plot(self.accY, pen=(29, 185, 84), name='Y')
        self.AccZLine = accGraph.plot(self.accZ, pen=(203, 45, 111), name='Z')
        accGraph.showGrid(x=True, y=True)

        gyroGraph = pg.PlotWidget(title='Gyro', background='#0f0f0f')
        gyroGraph.hideAxis('bottom')
        gyroGraph.addLegend()
        self.gyroPitch = [0] * 30
        self.gyroRoll = [0] * 30
        self.gyroYaw = [0] * 30
        self.gyroPitchLine = gyroGraph.plot(self.gyroPitch, pen=(102, 252, 241), name='Pitch')
        self.gyroRollLine = gyroGraph.plot(self.gyroRoll, pen=(29, 185, 84), name='Roll')
        self.gyroYawLine = gyroGraph.plot(self.gyroYaw, pen=(203, 45, 111), name='Yaw')
        gyroGraph.showGrid(x=True, y=True)

        pressureGraph = pg.PlotWidget(title='Barometric pressure', background='#0f0f0f')
        self.pressureData = [0] * 30
        self.pressureLine = pressureGraph.plot(self.pressureData, pen=(102, 252, 241))
        pressureGraph.showGrid(x=True, y=True)

        tempGraph = pg.PlotWidget(title='Temperature (ºc)', background='#0f0f0f')
        self.tempData = [0] * 30
        self.tempLine = tempGraph.plot(self.tempData, pen=(0, 255, 0))
        tempGraph.showGrid(x=True, y=True)

        font = pg.Qt.QtGui.QFont()
        font.setPixelSize(45)

        timeGraph = pg.PlotWidget(title='Time (s)', background='#0f0f0f')
        timeGraph.hideAxis('bottom')
        timeGraph.hideAxis('left')
        self.timeText = pg.TextItem('test', anchor=(0.5, 0.5), color='w')
        self.timeText.setFont(font)
        timeGraph.addItem(self.timeText)

        batteryGraph = pg.PlotWidget(title='battery satus', background='#0f0f0f')
        batteryGraph.hideAxis('bottom')
        batteryGraph.hideAxis('left')
        self.batteryText = pg.TextItem('test', anchor=(0.5, 0.5), color='w')
        self.batteryText.setFont(font)
        batteryGraph.addItem(self.batteryText)

        freeFallGraph = pg.PlotWidget(title='Free fall', background='#0f0f0f')
        freeFallGraph.hideAxis('bottom')
        freeFallGraph.hideAxis('left')
        self.freeFallText = pg.TextItem('test', anchor=(0.5, 0.5), color='w')
        self.freeFallText.setFont(font)
        freeFallGraph.addItem(self.freeFallText)

        baseLayout = QGridLayout()

        title = QLabel('@IamRezaMousavi')
        title.setStyleSheet(
            """QLabel
                            {
                                color: gray;
                            }
                            """,
        )
        title.setFont(QFont('ComicSansMS', 7))
        title.setAlignment(Qt.AlignCenter)

        baseLayout.addWidget(exitButton, 0, 25)

        titleLayout = QGridLayout()
        titleLayout.addWidget(title)
        baseLayout.addLayout(titleLayout, 0, 0, 1, 25)

        buttonLayout = QGridLayout()
        buttonLayout.addWidget(self.combobox, 0, 0)
        buttonLayout.addWidget(startButton, 1, 0)
        buttonLayout.addWidget(stopButton, 2, 0)
        buttonLayout.addWidget(clearButton, 3, 0)
        baseLayout.addLayout(buttonLayout, 1, 0, 4, 1)

        saveLayout = QGridLayout()
        fileNameLabel = QLabel('File Name')
        fileNameLabel.setStyleSheet(
            """QLabel
                                    {
                                        color: white;
                                    }
                                    """,
        )
        fileNameLabel.setFont(QFont('Arial', 10))
        saveLayout.addWidget(fileNameLabel, 0, 0)

        self.fileNameBox = QLineEdit()
        self.fileNameBox.setPlaceholderText('DataFileName')
        self.fileNameBox.returnPressed.connect(lambda: self.startStorageFunc())
        self.fileName = self.fileNameBox.text()
        saveLayout.addWidget(self.fileNameBox, 0, 1)

        startStorage = QPushButton('Start Storage')
        startStorage.clicked.connect(self.startStorageFunc)
        startStorage.setStyleSheet(
            """QPushButton
                                 {
                                     background: transparent;
                                     color: white;
                                     border: 1px solid;
                                     border-radius: 5px;
                                     border-color: green;
                                     font: 14px;
                                 }
                                 QPushButton:pressed
                                 {
                                     background-color: green;
                                     color: black;
                                 }
                                 """,
        )
        stopStorage = QPushButton('Stop Storage')
        stopStorage.clicked.connect(self.stopStorageFunc)
        stopStorage.setStyleSheet(
            """QPushButton
                                 {
                                     background: transparent;
                                     color: white;
                                     border: 1px solid;
                                     border-radius: 5px;
                                     border-color: red;
                                     font: 14px;
                                 }
                                 QPushButton:pressed
                                 {
                                     background-color: red;
                                     color: black;
                                 }
                                 """,
        )

        self.fileNameShow = QLabel('')
        self.fileNameShow.setStyleSheet(
            """QLabel
                                    {
                                        color: white;
                                    }
                                    """,
        )
        self.fileNameShow.setFont(QFont('Arial', 10))
        self.fileNameShow.setAlignment(Qt.AlignCenter)

        saveLayout.addWidget(startStorage, 1, 0)
        saveLayout.addWidget(stopStorage, 1, 1)
        saveLayout.addWidget(self.fileNameShow, 2, 0, 1, 2)
        baseLayout.addLayout(saveLayout, 6, 0)

        fristPlotLayout = QGridLayout()
        fristPlotLayout.addWidget(graphWidget, 0, 0, 1, 2)
        fristPlotLayout.addWidget(speedGraph, 0, 2, 1, 2)
        baseLayout.addLayout(fristPlotLayout, 1, 1, 5, 20)

        secondPlotLayout = QGridLayout()
        secondPlotLayout.addWidget(accGraph, 0, 1)
        secondPlotLayout.addWidget(gyroGraph, 0, 2)
        secondPlotLayout.addWidget(pressureGraph, 0, 3)
        secondPlotLayout.addWidget(tempGraph, 0, 4)
        baseLayout.addLayout(secondPlotLayout, 6, 1, 5, 20)

        textPlotLayout = QGridLayout()
        textPlotLayout.addWidget(timeGraph, 0, 0, 1, 2)
        textPlotLayout.addWidget(batteryGraph, 1, 0, 1, 2)
        textPlotLayout.addWidget(freeFallGraph, 2, 0, 1, 2)
        baseLayout.addLayout(textPlotLayout, 1, 21, 10, 5)

        box = QGroupBox(self)
        box.setLayout(baseLayout)
        box.setStyleSheet(
            """QGroupBox
                          {
                              background-color: rgba(0, 0, 0, 200)
                          }
                          """,
        )
        self.setCentralWidget(box)

        self.oldPos = self.pos()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.oldPos)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.oldPos = event.globalPos()

    def updateGraphWidget(self, data):
        newValue = float(data[1])
        self.xValues = self.xValues[1:]
        self.xValues.append(self.xValues[-1] + 1)
        self.yValues[:-1] = self.yValues[1:]
        self.yValues[-1] = newValue
        self.data_line.setData(self.xValues, self.yValues)

    def updateSpeedGraph(self, data):
        vzo = float(data[10])
        self.vx += float(data[8]) * 500
        self.vy += float(data[9]) * 500
        self.vz += (float(data[10]) - vzo) * 500
        sum = pow(self.vx, 2) + pow(self.vy, 2) + pow(self.vz, 2)
        newValue = sqrt(sum)
        self.speedData[:-1] = self.speedData[1:]
        self.speedData[-1] = newValue
        self.speedGraphPtr += 1
        self.speedGraphLine.setData(self.speedData)
        self.speedGraphLine.setPos(self.speedGraphPtr, 0)

    def updateAccPlot(self, data):
        self.accX[:-1] = self.accX[1:]
        self.accY[:-1] = self.accY[1:]
        self.accZ[:-1] = self.accZ[1:]

        self.accX[-1] = float(data[8])
        self.accY[-1] = float(data[9])
        self.accZ[-1] = float(data[10])

        self.AccXLine.setData(self.accX)
        self.AccYLine.setData(self.accY)
        self.AccZLine.setData(self.accZ)

    def updateGyroPlot(self, data):
        self.gyroPitch[:-1] = self.gyroPitch[1:]
        self.gyroRoll[:-1] = self.gyroRoll[1:]
        self.gyroYaw[:-1] = self.gyroYaw[1:]

        self.gyroPitch[-1] = float(data[5])
        self.gyroRoll[-1] = float(data[6])
        self.gyroYaw[-1] = float(data[7])

        self.gyroPitchLine.setData(self.gyroPitch)
        self.gyroRollLine.setData(self.gyroRoll)
        self.gyroYawLine.setData(self.gyroYaw)

    def updatePressurePlot(self, data):
        self.pressureData[:-1] = self.pressureData[1:]
        self.pressureData[-1] = float(data[4])
        self.pressureLine.setData(self.pressureData)

    def updateTempPlot(self, data):
        self.tempData[:-1] = self.tempData[1:]
        self.tempData[-1] = float(data[3])
        self.tempLine.setData(self.tempData)

    def updateTimeText(self, data):
        # temp = round(int(value_chain[0]) / 60000, 2)
        temp = round(float(data[0]), 2)
        self.timeText.setText(f'{temp:.2f}')

    def updateBattery(self, data):
        pass

    def updateFreeFall(self, data):
        if data[2] == '0':
            self.freeFallText.setText('No')
        else:
            self.freeFallText.setText('Yes')

    def startStorageFunc(self):
        self.fileName = self.fileNameBox.text()
        self.fileName = 'data' if self.fileName == '' else self.fileName
        self.fileNameShow.setText('will be save in ' + self.fileName + '.csv')
        self.dataBase.start()

    def stopStorageFunc(self):
        self.dataBase.stop()
        self.fileNameShow.setText('NOT saving')

    def updatePlotData(self):
        if self.ser.isOpen() or self.ser.dummyMode:
            data = self.ser.getData()
            self.updateGraphWidget(data)
            self.updateSpeedGraph(data)
            self.updateAccPlot(data)
            self.updateGyroPlot(data)
            self.updatePressurePlot(data)
            self.updateTempPlot(data)
            self.updateTimeText(data)
            self.updateBattery(data)
            self.updateFreeFall(data)
            self.dataBase.guardar(data, self.fileName)

    def startPloting(self):
        portName = self.combobox.currentText()
        self.ser = Communication(portName)
        self.timer = QTimer()
        self.timer.setInterval(150)  # 50 ns
        self.timer.timeout.connect(self.updatePlotData)
        self.timer.start()

    def stopPloting(self):
        self.ser.close()
        self.ser.dummyMode = False

    def clearPloting(self):
        self.xValues = list(range(30))
        self.yValues = [0] * 30
        self.data_line.setData(self.xValues, self.yValues)
        self.speedData = [0] * 30
        self.speedGraphLine.setData(self.speedData)
        self.accX = [0] * 30
        self.AccXLine.setData(self.accX)
        self.accY = [0] * 30
        self.AccYLine.setData(self.accY)
        self.accZ = [0] * 30
        self.AccZLine.setData(self.accZ)
        self.gyroPitch = [0] * 30
        self.gyroPitchLine.setData(self.gyroPitch)
        self.gyroRoll = [0] * 30
        self.gyroRollLine.setData(self.gyroRoll)
        self.gyroYaw = [0] * 30
        self.gyroYawLine.setData(self.gyroYaw)
        self.pressureData = [0] * 30
        self.pressureLine.setData(self.pressureData)
        self.tempData = [0] * 30
        self.tempLine.setData(self.tempData)
        self.timeText.setText('test')
        self.batteryText.setText('test')
        self.freeFallText.setText('test')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())
