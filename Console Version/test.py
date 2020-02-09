# -*- coding: utf-8 -*-

'''
    【简介】
    PyQt5中QButton例子
'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        layout = QVBoxLayout()   #设置垂直布局

        self.btn1 = QPushButton("Button1")
        # setChenkable()：设置按钮是否已经被选中，true表示按钮将被保持已点击和释放状态
        self.btn1.setCheckable(True)
        # toggle()：在按钮之间进行切换
        self.btn1.toggle()
        # 通过lambda方式来传递额外的参数btn1，将clicked信号发送给槽函数whichbtn()
        self.btn1.clicked.connect(lambda:self.whichbtn(self.btn1) )
        self.btn1.clicked.connect(self.btnstate)
        layout.addWidget(self.btn1)

        self.btn2 = QPushButton('image')
        self.btn2.setIcon(QIcon(QPixmap("./images/python.png")))
        self.btn2.clicked.connect(lambda:self.whichbtn(self.btn2) )
        layout.addWidget(self.btn2)
        self.setLayout(layout)

        self.btn3 = QPushButton("Disabled")
        # setEnabled()：设置按钮是否可用，false时按钮变成不可用状态，点击它不会发送信号
        self.btn3.setEnabled(False)
        layout.addWidget(self.btn3)

        self.btn4= QPushButton("&Download")
        self.btn4.setDefault(True)  #设置按钮的默认状态
        self.btn4.clicked.connect(lambda:self.whichbtn(self.btn4))
        layout.addWidget(self.btn4)
        self.setWindowTitle("Button demo")

    def btnstate(self):
        if self.btn1.isChecked():  #返回按钮的状态
            print("button pressed" )

        else:
            print("button released" )

    def whichbtn(self,btn):
        print("clicked button is " + btn.text() )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    btnDemo = Form()
    btnDemo.show()
    sys.exit(app.exec_())