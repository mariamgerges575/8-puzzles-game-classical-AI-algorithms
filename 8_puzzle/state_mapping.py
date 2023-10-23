
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
    
    
    
def get_path(parent, goalTest):
    answer = []
    state = goalTest
    while parent[state] != state:
        answer.append(state)
        state = parent[state]
    answer.append(state)
    answer.reverse()
    boards=[]
    for binaryState in answer:
        boardState = to_board(binaryState)
        boards.append(boardState)
    cost = len(answer) - 1
    return boards,cost
    
def printboard(state):
    board=to_board(state)
    print(board[0],board[1],board[2],"________________________________________________________________",sep="\n")