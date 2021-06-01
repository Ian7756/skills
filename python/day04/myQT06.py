import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5 import QtWidgets

Ui_MainWindow, QtBaseClass = uic.loadUiType("myQT06.ui")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
        
        
        btn = [self.ui.pb1,self.ui.pb2,self.ui.pb3,self.ui.pb4,self.ui.pb5,self.ui.pb6,self.ui.pb7,self.ui.pb8,self.ui.pb9,self.ui.pb0]
        self.ui.pb10.clicked.connect(self.btn_call)
        for i in range(10):
            btn[i].clicked.connect(self.btn_clicked)
        
    def btn_call(self):
        QtWidgets.QMessageBox.about(self,"Calling", self.ui.le.text())
    
    def btn_clicked(self):
        resStr = self.sender().text()
        self.ui.le.setText(self.ui.le.text()+resStr)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()           
    app.exec_()

