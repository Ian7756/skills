import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("myQT05.ui")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
  
        self.ui.pb.clicked.connect(self.btn_clicked)
 
    def btn_clicked(self):
        val1 = int(self.ui.le1.text())
        val2 = int(self.ui.le2.text())
        result = 0
        for i in range(val1,val2+1):
            result += i
        self.ui.le3.setText(str(result))
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()           
    app.exec_()

