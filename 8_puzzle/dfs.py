import datetime


def get_value(position, binary):
    return binary >> (36 - position * 4) & 0xf


def change_value(position, new_value, binary):
    clear = 0xffffffffff & ~(0xf << (36 - position * 4))
    set = new_value << (36 - position * 4)
    return binary & clear | set


def to_binary(board):
    result = 0
    for row in range(3):
        for col in range(3):
            result += board[row][col] << (32 - (row * 3 + col) * 4)
            if board[row][col] == 0:
                result += (row * 3 + col + 1) << 36
    return result


def to_board(binary):
    board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    for cell in range(9):
        board[cell // 3][cell % 3] = get_value(cell + 1, binary)
    return board


def input_board():
    board = []
    for i in range(3):
        row = input().split(' ')
        row2 = []
        for j in row:
            row2.append(int(j))
        board.append(row2)

    return board


def solvable(board):
    prev = []
    inversions = 0
    for row in board:
        for cell in row:
            if cell == 0:
                continue
            for e in prev:
                if e > cell:
                    inversions += 1
            prev.append(cell)
    if inversions % 2:
        return False
    return True


def show_path(parent, goalTest):
    answer = []
    state = goalTest
    while parent[state] != state:
        answer.append(state)
        state = parent[state]
    answer.append(state)
    answer.reverse()
    for binaryState in answer:
        boardState = to_board(binaryState)
        for row in boardState:
            print(row)
        print('_' * 50)
    cost = len(answer) - 1
    print(f'Cost = {cost}')


def depth_first_search(initial_state, goal_test):
    stack = [(initial_state << 20) + 1]
    expanded = set()
    parent = {initial_state: initial_state}
    nodes_expanded = 0
    maximum_depth = 1
    while len(stack) > 0:
        state = stack.pop()
        depth = state & 0xfffff
        maximum_depth = max(maximum_depth, depth)
        state = state >> 20
        expanded.add(state)
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
            if new_state in expanded or new_state in parent:
                continue
            parent[new_state] = state
            new_state = (new_state << 20) | depth+1
            stack.append(new_state)

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
        depth_first_search(to_binary(board), binary_goal)
    else:
        print("NOT SOLVABLE")
    running_time = datetime.datetime.now() - time
    print(f'Running Time = {running_time.microseconds} microseconds')
