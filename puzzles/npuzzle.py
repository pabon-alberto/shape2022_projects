"""
SHAPE Summer 2022

In this assignment you will implement and compare different search strategies
for solving the n-Puzzle, which is a generalization of the 8 and 15 puzzle to
squares of arbitrary size (we will only test it with 8-puzzles for now). 
See Courseworks for detailed instructions.
"""

from genericpath import exists
import time

def state_to_string(state):
    row_strings = [" ".join([str(cell) for cell in row]) for row in state]
    return "\n".join(row_strings)


def swap_cells(state, i1, j1, i2, j2):
    """
    Returns a new state with the cells (i1,j1) and (i2,j2) swapped. 
    """
    value1 = state[i1][j1]
    value2 = state[i2][j2]
    
    new_state = []
    for row in range(len(state)): 
        new_row = []
        for column in range(len(state[row])): 
            if row == i1 and column == j1: 
                new_row.append(value2)
            elif row == i2 and column == j2:
                new_row.append(value1)
            else: 
                new_row.append(state[row][column])
        new_state.append(tuple(new_row))
    return tuple(new_state)
    

def get_successors(state):
    """
    This function returns a list of possible successor states resulting
    from applicable actions. 
    The result should be a list containing (Action, state) tuples. 
    For example [("Up", ((1, 4, 2),(0, 5, 8),(3, 6, 7))), 
                 ("Left",((4, 0, 2),(1, 5, 8),(3, 6, 7)))] 
    """ 
    child_states = []

    for row in range(len(state)):
        for column in range(len(state[row])):
            if state[row][column] == 0:
                if column < len(state)-1: # Left 
                    new_state = swap_cells(state, row,column, row, column+1)
                    child_states.append(("Left", new_state))
                if column > 0: # Right 
                    new_state = swap_cells(state, row,column, row, column-1)
                    child_states.append(("Right", new_state))
                if row < len(state)-1:   #Up 
                    new_state = swap_cells(state, row,column, row+1, column)
                    child_states.append(("Up", new_state))
                if row > 0: # Down
                    new_state = swap_cells(state, row,column, row-1, column)
                    child_states.append(("Down", new_state))
                break
    return child_states

            
def goal_test(state):
    """
    Returns True if the state is a goal state, False otherwise. 
    """    
    counter = 0
    for row in state:
        for cell in row: 
            if counter != cell: 
                return False 
            counter += 1
    return True
   
def bfs(next_state):
    """
    Breadth first search.
    Returns A list of actions
    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """
    prev = {}
    actions = {} # for each discovered state,
                 # what is the action that 
                 # took you there

    # Write code here for bfs. 
    discovered = set()
    discovered.add(next_state)
    queue = []
    queue.append(next_state)
    discovered.add(next_state)
    ori_state = next_state

    total_visited_states = 0
    while len(queue) > 0:
        curr_state = queue.pop(0)
        successors = get_successors(curr_state)

        for element in successors:
            next_action = element[0]
            next_state = element[1]
            if next_state not in discovered:
                total_visited_states += 1
                discovered.add(next_state)
                queue.append(next_state)
                prev[next_state] = curr_state
                if next_state in actions:
                    actions[next_state] = element
                else:
                    actions[next_state] = next_action
                if goal_test(next_state):
                    state = next_state
                    prev_state = prev[state]
                    prev_action = actions[state]
                    returnls_state = [prev_state]
                    returnls_action = [prev_action]
                    while state != ori_state:
                        prev_state = prev.get(state)
                        prev_action = actions.get(prev_state)
                        returnls_action = [prev_action] + returnls_action
                        returnls_state = [prev_state] + returnls_state
                        state = prev_state
                    returnls_action = returnls_action[1:len(returnls_action)]
                    # print(returnls_action)
                    # print(total_visited_states)
                    return(returnls_action)
        # total_visited_states +=1     

    #print("Total visited states:", total_visited_states)
                               
     
def dfs(state):
    """
    Depth first search.
    Returns: A list of actions.
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    prev = {}
    actions = {}
    
    #Write code here for dfs
    
    discovered = set()
    discovered.add(state)
    stack = []
    stack.append(state)
    discovered.add(state)
    ori_state = state

    total_visited_states = 0
    while len(stack) > 0:
        curr_state = stack.pop()
        successors = get_successors(curr_state)

        for element in successors:
            next_action = element[0]
            state = element[1]
            if state not in discovered:
                total_visited_states += 1
                discovered.add(state)
                stack.append(state)
                prev[state] = curr_state
                if state in actions:
                    actions[state] = element
                else:
                    actions[state] = next_action
                if goal_test(state):
                    state = state
                    prev_state = prev[state]
                    prev_action = actions[state]
                    returnls_state = [prev_state]
                    returnls_action = [prev_action]
                    while state != ori_state:
                        prev_state = prev.get(state)
                        prev_action = actions.get(prev_state)
                        returnls_action = [prev_action] + returnls_action
                        returnls_state = [prev_state] + returnls_state
                        state = prev_state
                    returnls_action = returnls_action[1:len(returnls_action)]
                    # print(returnls_action)
                    # print(total_visited_states)
                    return(returnls_action)
    
                
    # No solution found


def misplaced_heuristic(state):
    """
    Returns the number of misplaced tiles.
    """
    index = 0
    misplaced = 0
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] != index:
                misplaced += 1
                index += 1
    return misplaced # replace this


def manhattan_heuristic(state):
    """
    For each misplaced tile, compute the manhattan distance between the current
    position and the goal position. THen sum all distances. 
    """
    total_dist = 0
    for i in range(len(state)): #y coordinate
        for j in range(len(state[i])): #x coordinate
            index = state[i][j]
            if index != 0:
                correctX = index%3
                correctY = index//3
                distance = abs(j - correctX) + abs(i - correctY)
                total_dist += distance
                
    return total_dist # replace this


def greedy(state, heuristic = misplaced_heuristic):
    """
    Greedy search is a variant of depth-first search that uses a heuristic to 
    select the next state from the immediate successor states.  
    Returns three values: A list of actions.

    Should print:  the number of states expanded, and the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here
    actions = {}
    costs = {}
    prev = {}

    costs[state] = 0

    discovered = set()
    discovered.add(state)
    stack = []
    stack.append(state)
    discovered.add(state)
    ori_state = state #Starting state

    total_visited_states = 0
    while len(stack) > 0:
        curr_state = stack.pop()
        successors = get_successors(curr_state)
        successors.sort(key = lambda tup:heuristic(tup[1]), reverse = True)

        for element in successors:
            next_action = element[0]
            state = element[1]
            if state not in discovered:
                total_visited_states += 1
                discovered.add(state)
                stack.append(state)
                prev[state] = curr_state
                if state in actions:
                    actions[state] = element
                else:
                    actions[state] = next_action
                if goal_test(state):
                    prev_state = prev[state]
                    prev_action = actions[state]
                    returnls_state = [prev_state]
                    returnls_action = [prev_action]
                    while state != ori_state:
                        prev_state = prev.get(state)
                        prev_action = actions.get(prev_state)
                        returnls_action = [prev_action] + returnls_action
                        returnls_state = [prev_state] + returnls_state
                        state = prev_state
                    returnls_action = returnls_action[1:len(returnls_action)]
                    # print(returnls_action)
                    # print(total_visited_states)
                    return(returnls_action)
    
    # Write best first search here.

    return None # No solution found


def best_first(state, heuristic = misplaced_heuristic):
    """
    Breadth first search using the heuristic function passed as a parameter.
    Returns: A list of actions
    Should print: the number of states visited, and the maximum size of the frontier.  
    """

    # You might want to use these functions to maintain a priority queue 
    # You may also use your own heap class here
    from heapq import heappush
    from heapq import heappop

    heap = []
    
    heappush(heap, (heuristic(state), state))
    actions = {}

    # Write best first search here.
    
    prev = {}

    discovered = set()
    discovered.add(state)
    ori_state = state

    total_visited_states = 0
    while len(heap) > 0:
        n, curr_state = heappop(heap) #n is the number, curr_state is the state
        successors = get_successors(curr_state)

        for element in successors:
            next_action = element[0]
            state = element[1]
            if state not in discovered:
                total_visited_states += 1
                discovered.add(state)
                heappush(heap, (heuristic(state), state))
                prev[state] = curr_state
                if state in actions:
                    actions[state] = element
                else:
                    actions[state] = next_action
                if goal_test(state):
                    state = state
                    prev_state = prev[state]
                    prev_action = actions[state]
                    returnls_state = [prev_state]
                    returnls_action = [prev_action]
                    while state != ori_state:
                        prev_state = prev.get(state)
                        prev_action = actions.get(prev_state)
                        returnls_action = [prev_action] + returnls_action
                        returnls_state = [prev_state] + returnls_state
                        state = prev_state
                    returnls_action = returnls_action[1:len(returnls_action)]
                    # print(returnls_action)
                    # print(total_visited_states)
                    return(returnls_action)
        # total_visited_states +=1     
   #print("Total visited states:", total_visited_states)



def astar(state, heuristic): #If heuristic is admissible, A* search is optimal.
    """
    A-star search using the heuristic function passed as a parameter. 
    Returns: A list of actions
    Should print: the number of states expanded, and the maximum size of the frontier.  
    """
    # You might want to use these functions to maintain a priority queue
    # You may also use your own heap class here

    from heapq import heappush
    from heapq import heappop

    actions = {}
    costs = {}

    costs[state] = 0
    
    # Write A* search here

    heap = []
    
    heappush(heap, (heuristic(state) + costs[state], state))
    actions = {}

    # Write best first search here.
    
    prev = {}
    discovered = set()
    discovered.add(state)
    ori_state = state

    total_visited_states = 0
    while len(heap) > 0:
        n, curr_state = heappop(heap) #n is the number, curr_state is the state
        successors = get_successors(curr_state)
        for element in successors:
            next_action = element[0]
            state = element[1]
            if state not in discovered:
                total_visited_states += 1
                discovered.add(state)
                costs[state] = costs[curr_state] + 1
                heappush(heap, (heuristic(state) + costs[state], state))
                prev[state] = curr_state
                if state in actions:
                    actions[state] = element
                else:
                    actions[state] = next_action
                if goal_test(state):
                    state = state
                    prev_state = prev[state]
                    prev_action = actions[state]
                    returnls_state = [prev_state]
                    returnls_action = [prev_action]
                    while state != ori_state:
                        prev_state = prev.get(state)
                        prev_action = actions.get(prev_state)
                        returnls_action = [prev_action] + returnls_action
                        returnls_state = [prev_state] + returnls_state
                        state = prev_state
                    returnls_action = returnls_action[1:len(returnls_action)]
                    # print(returnls_action) #prints list of actions
                    # print(total_visited_states) # prints number of total visited areas
                    return(returnls_action)



def print_result(solution):
    """
    Helper function to format test output. 
    """
    if solution is None: 
        print("No solution found.")
    else: 
        print("Solution has {} actions.".format(len(solution)))

if __name__ == "__main__":

    #Easy test case
    test_state = ((1, 4, 2),
                  (0, 5, 8), 
                  (3, 6, 7)) 

    #More difficult test case
    # test_state = ((7, 2, 4),
    #              (8, 3, 1),
    #              (5, 0, 6))
    
    print(state_to_string(test_state))
    print()

    print("Misplaced:", misplaced_heuristic(test_state))
    print('\n====Manhattan====\n'+'Distance from original state:', manhattan_heuristic(test_state))
    
    print("====BFS====")
    start = time.time()
    solution = bfs(test_state) 
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))

    
    print() 
    print("====DFS====") 
    start = time.time()
    solution = dfs(test_state)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))

    print()
    print("====Greedy====") 
    start = time.time()
    solution = greedy(test_state, manhattan_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    

    print() 
    print("====Best-First====") 
    start = time.time()
    solution = best_first(test_state, manhattan_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
    
    print() 
    print("====A*====") 
    start = time.time()
    solution = astar(test_state, manhattan_heuristic)
    end = time.time()
    print_result(solution)
    print("Total time: {0:.3f}s".format(end-start))
