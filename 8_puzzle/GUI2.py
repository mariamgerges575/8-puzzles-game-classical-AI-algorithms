import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from dfs import*
from bfs import*
import datetime
class Window(QMainWindow):
    
    def __init__(self,initial,path):
        super().__init__()
        self.path=path
        self.currentInd=0
        self.setWindowTitle("8 puzzles") 
        self.layout2= QGridLayout()
        # setting geometry 
        
        self.setGeometry(100, 100, 225, 300) 
  
        # calling method 
        self.setupUi(initial) 
        self.btnLeft = QPushButton("\u2190", self) 
        self.btnRight = QPushButton("\u2192", self) 
        self.btnLeft.setGeometry(0, 225, 112, 75)
        self.btnRight.setGeometry(112, 225, 112, 75)
        self.btnLeft.setFont(QFont('Arial', 15))
        self.btnRight.setFont(QFont('Arial', 15))
        self.btnLeft.clicked.connect(self.go_left) 
        self.btnRight.clicked.connect(self.go_right) 
        # showing all the widgets 
        self.show() 
        
    def setupUi(self,state):
        self.button0 = QPushButton(str(state[0][0]), self) 
        self.button1 = QPushButton(str(state[0][1]), self) 
        self.button2 = QPushButton(str(state[0][2]), self) 
        
        self.button3 = QPushButton(str(state[1][0]), self) 
        self.button4 = QPushButton(str(state[1][1]), self) 
        self.button5 = QPushButton(str(state[1][2]), self) 
        
        self.button6 = QPushButton(str(state[2][0]), self) 
        self.button7 = QPushButton(str(state[2][1]), self) 
        self.button8 = QPushButton(str(state[2][2]), self) 
        
        # setting geometry of radio button 
        self.button0.setGeometry(0, 0, (state[0][0]>0)*75, 75) 
        self.button1.setGeometry(75, 0,(state[0][1]>0)*75, 75) 
        self.button2.setGeometry(150, 0,(state[0][2]>0)*75, 75) 
        
        self.button3.setGeometry(0, 75, (state[1][0]>0)*75, 75) 
        self.button4.setGeometry(75, 75, (state[1][1]>0)*75, 75) 
        self.button5.setGeometry(150, 75,(state[1][2]>0)*75, 75) 
        
        self.button6.setGeometry(0, 150, (state[2][0]>0)*75, 75)
        self.button7.setGeometry(75, 150, (state[2][1]>0)*75, 75) 
        self.button8.setGeometry(150, 150,(state[2][2]>0)* 75, 75) 
        
        self.button0.setFont(QFont('Arial', 15))
        self.button1.setFont(QFont('Arial', 15))
        self.button2.setFont(QFont('Arial', 15))
        self.button3.setFont(QFont('Arial', 15))
        self.button4.setFont(QFont('Arial', 15))
        self.button5.setFont(QFont('Arial', 15))
        self.button6.setFont(QFont('Arial', 15))
        self.button7.setFont(QFont('Arial', 15))
        self.button8.setFont(QFont('Arial', 15))

        
    def draw(self,state):
        self.button0.setText(str(state[0][0])) 
        self.button1.setText(str(state[0][1])) 
        self.button2.setText(str(state[0][2])) 
        
        self.button3.setText(str(state[1][0])) 
        self.button4.setText(str(state[1][1])) 
        self.button5.setText(str(state[1][2])) 
        
        self.button6.setText(str(state[2][0])) 
        self.button7.setText(str(state[2][1])) 
        self.button8.setText(str(state[2][2])) 
        
        # setting geometry of radio button 
        self.button0.setGeometry(0, 0, (state[0][0]>0)*75, 75) 
        self.button1.setGeometry(75, 0,(state[0][1]>0)* 75, 75) 
        self.button2.setGeometry(150, 0,(state[0][2]>0)* 75, 75) 
        
        self.button3.setGeometry(0, 75, (state[1][0]>0)*75, 75) 
        self.button4.setGeometry(75, 75, (state[1][1]>0)*75, 75) 
        self.button5.setGeometry(150, 75,(state[1][2]>0)* 75, 75) 
        
        self.button6.setGeometry(0, 150, (state[2][0]>0)*75, 75) 
        self.button7.setGeometry(75, 150, (state[2][1]>0)*75, 75) 
        self.button8.setGeometry(150, 150,(state[2][2]>0)*75, 75) 
        
        # creating push button 
        
  
        # connect push button to method 
      
    def go_left(self): 
        if(self.currentInd==0):
            return
        else:
            self.currentInd-=1
            self.draw(self.path[self.currentInd])
        # setting new text to radio button 
        
        
    def go_right(self):
        if(self.currentInd== len(self.path)-1):
            return
        else:
            self.currentInd+=1
            self.draw(self.path[self.currentInd])
            
if __name__ == "__main__":
    binary_goal = 0x1012345678
    board_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    board = input_board()
    time = datetime.datetime.now()
    if solvable(board):
        bol,path,cost=depth_first_search(to_binary(board), binary_goal)
        running_time = datetime.datetime.now() - time
        print(f'Running Time = {running_time.microseconds} microseconds')

        
    else:
        print("NOT SOLVABLE")
    

