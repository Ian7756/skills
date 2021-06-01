import sys
import numpy as np
import pymysql
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic, QtGui, QtWidgets
from sqlalchemy.sql.expression import true

Ui_MainWindow, QtBaseClass = uic.loadUiType("omok04.ui")


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(QSize(920,900))
        self.gameSize = 10
        
        self.flag_turn = True
        self.flag_playing = True
        
        self.omock_db = []
        self.arr2d = []
        self.makeArr()
        self.pb2d = []
        self.ui.pb_reset.clicked.connect(self.resetGame)
            
        for i in range(len(self.arr2d)):
            pb_row = []
            for j in range(self.arr2d[i].__len__()):
                pb=QPushButton("",self)
                pb.setIcon(QIcon("0.png"))
                pb.setIconSize(QSize(40,40))
                pb.setGeometry(40*j+20,40*i+20,40,40)
                pb.clicked.connect(self.pb_click)
                pb.setToolTip("{},{}".format(i,j))
                pb_row.append(pb)
            self.pb2d.append(pb_row)
        
        self.myRender()
        
        
        
    
    
    def myRender(self):
        for i in range(self.arr2d.__len__()):
            for j in range(self.arr2d[i].__len__()):
                if self.arr2d[i][j] == 1:
                    self.pb2d[i][j].setIcon(QIcon("1.png"))
                elif self.arr2d[i][j] == 2:
                    self.pb2d[i][j].setIcon(QIcon("2.png"))
                else :
                    self.pb2d[i][j].setIcon(QIcon("0.png"))
    
    
    def pb_click(self):
        if not self.flag_playing:
            QtWidgets.QMessageBox.about(self,"게임", "종료된 게임입니다")
            return
        idx = self.sender().toolTip().split(",")
        int_i = int(idx[0])
        int_j = int(idx[1])
        int_turn = 0
        
        if self.arr2d[int_i][int_j] > 0:
            QtWidgets.QMessageBox.about(self,"경고!", "이미 놓인 자리입니다")
            return
        
        if self.flag_turn:
            self.arr2d[int_i][int_j] = 1
            int_turn = 1
        else:
            self.arr2d[int_i][int_j] = 2
            int_turn = 2
        
        self.omock_db.append(str(self.arr2d).replace(".","").replace(" ","").replace("\n","").replace("[","").replace("]",""))
        
        winner = self.getWinner(int_i, int_j, int_turn)
        
        self.myRender()
        
        if winner:
            self.setOmockDb(self.omock_db, int_turn)
            QtWidgets.QMessageBox.about(self,"게임", "{}이 승리하였습니다".format("흑돌" if self.flag_turn else "백돌"))
            self.flag_playing = False
            

        self.flag_turn = not self.flag_turn


    def getUp(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                i += -1
                if i < 0 : 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getDW(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                i += +1
                if i < 0 : 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getLE(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                j += -1
                if j < 0 : 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getRI(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                j += +1
                if j < 0 : 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getUL(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                i += -1
                j += -1
                if i < 0 or j < 0: 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getDL(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                i += +1
                j += -1
                if i < 0 or j < 0: 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getUR(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                i += -1
                j += +1
                if i < 0 or j < 0: 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt
            
    def getDR(self,i,j,turn):
        cnt = 0
        while(True):
            try:
                i += +1
                j += +1
                if i < 0 or j < 0: 
                    return cnt
                if self.arr2d[i][j] == turn:
                    cnt += 1
                else:
                    return cnt
            except:
                return cnt

    def getWinner(self,i,j,turn):
        up = self.getUp(i, j, turn)
        dw = self.getDW(i, j, turn)
        le = self.getLE(i, j, turn)
        ri = self.getRI(i, j, turn)
        ul = self.getUL(i, j, turn)
        dl = self.getDL(i, j, turn)
        ur = self.getUR(i, j, turn)
        dr = self.getDR(i, j, turn)
        if 1+dl+ur == 5 or 1+ul+dr == 5 or 1+le+ri == 5 or 1+up+dw == 5 :
            return True
        else :
            return False
            
    def makeArr(self):
        self.arr2d = np.zeros((self.gameSize,self.gameSize))
        
    def resetGame(self):
        self.makeArr()
        self.myRender()
        self.flag_playing = True
        self.flag_turn = True
    
        
    def setOmockDb(self,o_history_list,win):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='java', db='mypy', charset='utf8')
        curs = conn.cursor()
        pan = self.getPan()
        for i,o_history in enumerate(o_history_list):
            sql = "insert into omock(pan,o_seq,o_history,win) values ("+str(pan)+","+str(i+1)+",'"+o_history+"',"+str(win)+")"
            curs.execute(sql)
        conn.commit()
        conn.close()
        
    def getPan(self):
        conn = pymysql.connect(host='127.0.0.1', user='root', password='java', db='mypy', charset='utf8')
        curs = conn.cursor()
        sql = "select COALESCE(max(pan),0)+1 from omock"
        curs.execute(sql)
        rows = curs.fetchall()
        pan = rows[0][0] 
        conn.close()
        return pan
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()           
    app.exec_()

