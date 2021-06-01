import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtGui

Ui_MainWindow, QtBaseClass = uic.loadUiType("omok01.ui")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        self.resize(QSize(400,400))
        
        self.arr2d = [
                [0,0,0,0,0, 0,0,0,0,0,],
                [0,0,0,0,0, 0,0,0,0,0,],
                [0,0,0,0,0, 0,0,0,0,0,],
                [0,0,0,0,0, 0,0,0,0,0,],
                [0,0,0,0,0, 0,0,0,0,0,],

                [0,0,0,0,1, 0,0,0,0,0,],
                [0,0,0,0,0, 0,0,0,0,0,],
                [0,0,0,0,0, 0,0,0,0,0,],
                [0,0,0,0,2, 0,0,0,0,0,],
                [0,0,0,0,0, 0,0,0,0,0,]
            ]
        
        self.pb2d = []
        
            
        for j in range(self.arr2d.__len__()):
            pb_row = []
            for i in range(self.arr2d[j].__len__()):
                pb=QPushButton("",self)
                pb.setIcon(QIcon("0.png"))
                pb.setIconSize(QSize(40,40))
                pb.setGeometry(40*j,40*i,40,40)
                pb.clicked.connect(self.pb_click)
                pb_row.append(pb)
            self.pb2d.append(pb_row)
        
        self.myRender()
    
    
    def myRender(self):
        for j in range(self.arr2d.__len__()):
            for i in range(self.arr2d[j].__len__()):
                if self.arr2d[j][i] == 1:
                    self.pb2d[j][i].setIcon(QIcon("1.png"))
                elif self.arr2d[j][i] == 2:
                    self.pb2d[j][i].setIcon(QIcon("2.png"))
                else :
                    self.pb2d[j][i].setIcon(QIcon("0.png"))
    
    def pb_click(self):
        print(self)
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()           
    app.exec_()

