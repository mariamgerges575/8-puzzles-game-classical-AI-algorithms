from dfs import *
import queue
import datetime

def breadth_first_search(initial_state, goal_test):
    frontier =queue.Queue()
    frontier .put(initial_state)
    expanded = set()
    parent = {initial_state: initial_state}
    nodes_expanded = 0
    while frontier.qsize() > 0:
        nodes_expanded += 1
        state = frontier.get()
        # printboard(state)
        expanded.add(state)
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
            if new_state in parent:
                continue
            parent[new_state] = state
            frontier.put(new_state)

    if goal_test not in parent:
        return False,None,None,nodes_expanded
    print("****************************** path from initial state to goal ****************************** ")
    show_path(parent, goal_test)
    path,cost=get_path(parent, goal_test)
    return True , path,cost,nodes_expanded

if __name__ == '__main__':
    binary_goal = 0x1012345678
    board_goal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    board = input_board()
    time = datetime.datetime.now()
    if solvable(board):
        breadth_first_search(to_binary(board), binary_goal)
    else:
        print("NOT SOLVABLE")
    running_time = datetime.datetime.now() - time
    print(f'Running Time = {running_time.microseconds} microseconds')