# import dfs as help
from math import sqrt
from dfs import *
from priorityQueue import PriorityQueue
def get_index(value):
    return int(value/3),value%3

def get_manhattan_value(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)

def get_euclidean_value(x1,x2,y1,y2):
    return sqrt(((abs(x1-x2)**2)) + ((y1-y2)**2))

def get_heuristic(state,H):
    sum = 0
    for i in range(1,10):
        value = get_value(i,state)
        x1,y1 = get_index(value)
        x2,y2 = get_index(i-1)
        sum += H(x1,x2,y1,y2)
    return sum

# def show_path_H(state):

    
#     boardState = to_board(state)
#     for row in boardState:
#         print(row)
#     print('_' * 50)

def show_path(parent, goalTest):
    answer = []
    state = goalTest
    while (parent[state])[0] != state:
        answer.append(state)
        state = (parent[state])[0]
    answer.append(state)
    answer.reverse()
    for binaryState in answer:
        boardState = to_board(binaryState)
        for row in boardState:
            print(row)
        print('_' * 50)
    cost = len(answer) - 1
    print(f'Cost = {cost}')

def A_Search(initial_state, goal_test,H,type):
    pq = PriorityQueue()
    pq.push((H(initial_state,type)+1,(initial_state<<20)+1))
    expanded = set()
    parent = {initial_state: (initial_state,1)}
    nodes_expanded = 0
    maximum_depth = 1
    while len(pq.elements) > 0:
        state = pq.pop()
        state = state[1]
        # print(state)
        if (state in expanded):
            continue
        depth = state & 0xfffff
        maximum_depth = max(maximum_depth, depth)
        state = state >> 20
        expanded.add(state)
        # show_path_H(state)
        nodes_expanded += 1
        if state == goal_test:
            break

        for i in [-3, -1, 1, 3]:
            pos = get_value(0, state)
            new_pos = pos + i
            if new_pos < 1 or new_pos > 9:
                continue
            if abs(i) == 1 and (max(pos, new_pos) == 4 or max(pos, new_pos) == 7):
                continue

            value = get_value(new_pos, state)
            new_state = change_value(pos, value, state)
            new_state = change_value(new_pos, 0, new_state)
            new_state = change_value(0, new_pos, new_state)
            # lw heya etxaret abl keda khlaassss
            if new_state in expanded:
                continue

            # if el depth elgeded 7yb2a as8r mn el adem
            # lw heya gededa 77othaaa 3latol
            if (new_state not in parent):
                # awel mra t3dy 3laayaaaaa
                pq.push((H(new_state,type)+depth+1,((new_state << 20) | depth+1)))
                parent[new_state]=(state,depth+1)

            elif (depth+1< parent[new_state][1]):
                parent[new_state]=(state,depth+1)
                pq.push((H(new_state,type)+depth+1,((new_state << 20) | depth+1)))


    if goal_test not in parent:
        return False

    show_path(parent, goal_test)
    print(f'Nodes Expanded = {nodes_expanded}')
    print(f'Search Depth = {maximum_depth}')
    return True

if __name__=='__main__':

    binary_goal = 0x1012345678
    board_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

    board = input_board()
    time = datetime.datetime.now()
    if solvable(board):
        initial_state = to_binary(board)
        A_Search(initial_state, binary_goal,get_heuristic,get_manhattan_value)
    else:
        print("NOT SOLVABLE")
    running_time = datetime.datetime.now() - time
    print(f'Running Time = {running_time.microseconds} microseconds')













if __name__=='__main__':
    #test manhatten ==16
    print(1)
    # print(get_heuristic_manhattan(0x1128456703,get_manhattan_value))
    print(get_heuristic(0x1128456703,get_euclidean_value))


