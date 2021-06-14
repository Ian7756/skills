# Qt Designer로 ui를 먼저 만들어보자 -> anaconda prompt에서 designer 입력해서 만든다음 임포트

import sys

# uic로 pyQt 설정..? 로드..?
from PyQt5 import uic

from PyQt5.QtWidgets import QMainWindow, QApplication


Ui_MainWindow, QtBaseClass = uic.loadUiType("qt_ui.ui")

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