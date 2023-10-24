import datetime
from dfs import*
from bfs import*
from state_mapping import*
from GUI2 import*
from A import*

binary_goal = 0x1012345678
board_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
algorithm=input("enter:\n1-Depth first search\n2-Breadth first search\n3-A*\n")
print("enter board row by row, numbers seperated with space")
board = input_board()


if solvable(board):
    if(algorithm=='1'):
        time = datetime.datetime.now()
        boolean,path,cost,nodes_expanded,maximum_depth=depth_first_search(to_binary(board), binary_goal)
        running_time = datetime.datetime.now() - time
        print(f'Cost = {cost}')
        print(f'Nodes Expanded = {nodes_expanded}')
        print(f'Search Depth = {maximum_depth}')
        print(f'Running Time = {running_time.microseconds} microseconds')
    elif(algorithm=='2'):
        time = datetime.datetime.now()
        boolean,path,cost,nodes_expanded=breadth_first_search(to_binary(board), binary_goal)
        running_time = datetime.datetime.now() - time
        print(f'Cost = {cost}')
        print(f'Nodes Expanded = {nodes_expanded}')
        print(f'Running Time = {running_time.microseconds} microseconds')
    elif(algorithm=='3'):
        print('1- manhattan')
        print('2- euclidean')
        type = input('')
        if type=='1':
            time = datetime.datetime.now()
            boolean,path,cost=A_Search(to_binary(board), binary_goal,get_heuristic,get_manhattan_value)
            running_time = datetime.datetime.now() - time
            print(f'Cost = {cost}')
            print(f'Running Time = {running_time.microseconds} microseconds')
        else:
            time = datetime.datetime.now()
            boolean,path,cost=A_Search(to_binary(board), binary_goal,get_heuristic,get_euclidean_value)
            running_time = datetime.datetime.now() - time
            print(f'Cost = {cost}')
            print(f'Running Time = {running_time.microseconds} microseconds')
                
        
    App = QApplication(sys.argv) 
    window = Window(board,path) 
    sys.exit(App.exec()) 
else:
    print("NOT SOLVABLE")


