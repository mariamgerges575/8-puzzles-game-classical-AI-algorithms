import datetime
from dfs import*
from bfs import*
from state_mapping import*
from GUI2 import*

binary_goal = 0x1012345678
board_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
algorithm=input("enter:\n1-Depth first search\n2-Breadth first search\n3-A*\n")
print("enter board row by row, numbers seperated with space")
board = input_board()


if solvable(board):
    if(algorithm=='1'):
        time = datetime.datetime.now()
        boolean,path,cost=depth_first_search(to_binary(board), binary_goal)
        running_time = datetime.datetime.now() - time
        print(f'Cost = {cost}')
        print(f'Running Time = {running_time.microseconds} microseconds')
    elif(algorithm=='2'):
        time = datetime.datetime.now()
        boolean,path,cost=breadth_first_search(to_binary(board), binary_goal)
        running_time = datetime.datetime.now() - time
        print(f'Cost = {cost}')
        print(f'Running Time = {running_time.microseconds} microseconds')
    App = QApplication(sys.argv) 
    window = Window(board,path) 
    sys.exit(App.exec()) 
else:
    print("NOT SOLVABLE")


