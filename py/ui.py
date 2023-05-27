# -*- coding: utf-8 -*-

import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import main_exec

def scriptRun(stage, times):
    # print('hello, wait 5 second')
    # for i in range(5):
    #     print(i+1)
    #     time.sleep(1)
    print('thread start')

class Gf_ui(QMainWindow):
    def __init__(self, parent=None):
        super(Gf_ui, self).__init__(parent)
        
        self.mainWidget = QWidget()
        self.scriptStatus = False

        mainLayout = QHBoxLayout()
        layout = QVBoxLayout()

        self.mainWidget.cb = QComboBox()
        self.mainWidget.cb.addItems(["12-4-e"])
        # self.mainWidget.cb.addItems(["1","2","3","4"])
        self.mainWidget.cb.currentText

        self.mainWidget.sb = QSpinBox()
        self.mainWidget.sb.setMinimum = 0
        self.mainWidget.sb.setMaximum = 100 + 1

        self.mainWidget.startBtn = QPushButton("start")
        self.mainWidget.startBtn.clicked.connect(self.testDisplay)
		
        self.logDisplay = QTextBrowser()

        layout.addStretch(2)
        layout.addWidget(self.mainWidget.cb)
        layout.addWidget(self.mainWidget.sb)
        layout.addStretch(1)
        layout.addWidget(self.mainWidget.startBtn)
        layout.addStretch(2)

        mainLayout.addItem(layout)
        mainLayout.addWidget(self.logDisplay)
        self.mainWidget.setLayout(mainLayout)

        self.setCentralWidget(self.mainWidget)
        self.setGeometry(800, 400, 400, 300)
        self.setWindowTitle("gf_script_manager")

        self.thread1 = testThread('test')

    def testDisplay(self): 
        battle = self.mainWidget.cb.currentText()
        times = self.mainWidget.sb.value()
        logStr = f"选择关卡:{battle}\t\t复刷次数:{times}"
        # print(logStr.encode('utf-8').decode('gbk'))
        self.logDisplay.append("<li>{} 准备开始关卡复刷：</li>".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        self.logDisplay.append("<li>{} ".format(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))+logStr+"</li>")
        self.thread1.config(stage=self.mainWidget.cb.currentText(), times=self.mainWidget.sb.value())
        self.startScript()

    def startScript(self):
        # self.mainWidget.startBtn.setText("running...")
        # self.scriptStatus = True
        self.thread1.start()

    def endScript(self):
        self.mainWidget.startBtn.setText("start")

class testThread(QThread):
    _signal = pyqtSignal(str)

    gameScript = main_exec.script()

    def __init__(self, parent):
        super(testThread, self).__init__()
        self.parent = parent

    def __del__(self):
        self.wait()

    def config(self, stage, times):
        self.gameScript.setConfig(battel_stage=stage, battel_times=times)

    def run(self):
        self.gameScript.run()

def main():
    app = QApplication(sys.argv)
    ui = Gf_ui()
    ui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

   