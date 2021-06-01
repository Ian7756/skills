import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("myQT03.ui")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
  
        self.ui.btn.clicked.connect(self.btn_clicked)
 
    def btn_clicked(self):
        val1 = int(self.ui.le1.text())
        val2 = int(self.ui.le2.text())
        self.ui.le3.setText(str(val1+val2))
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()           
    app.exec_()

