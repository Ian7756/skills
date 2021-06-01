import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("myQT01.ui")

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)      
  
        self.ui.pb.clicked.connect(self.btn_clicked)
 
    def btn_clicked(self):
        self.ui.lbl.setText("good evening")
 
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()           
    app.exec_()

