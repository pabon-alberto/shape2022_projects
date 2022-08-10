import random
import sys
import math

class FrozenLake(object):

    def __init__(self, width, height, targets, blocked, holes, start):
        self.initial_state = start 
        self.width = width
        self.height = height
        self.targets = set(targets)
        self.holes = set(holes)
        self.blocked = set(blocked)

        # Parameters for the simulation
        self.gamma = 0.9
        self.success_prob = 0.5
        self.fail_prob = 0.25

    def get_reward(self, state):
        if state in self.holes: 
            return -5.0 
        elif state in self.targets:
            return 1.0
        else: 
            return -0.1

    def print_map(self, policy=None):
        sys.stdout.write(" ")
        for i in range(self.width):
            sys.stdout.write("--")
        sys.stdout.write("\n")
        for j in range(self.height): 
            
            sys.stdout.write("|")
            for i in range(self.width): 
                if (i,j) in self.targets:
                    sys.stdout.write("T ")
                elif (i,j) in self.holes:  
                    sys.stdout.write("O ")
                elif (i,j) in self.blocked: 
                    sys.stdout.write("# ")
                else: 
                    if policy and (i,j) in policy:
                        a = policy[(i,j)]
                        if a=="n":
                            sys.stdout.write("^")
                        elif a=="s":
                            sys.stdout.write("v")
                        elif a=="e":
                            sys.stdout.write(">")
                        elif a=="w":
                            sys.stdout.write("<")
                        sys.stdout.write(" ")
                    elif (i,j)==self.initial_state:
                        sys.stdout.write("* ")
                    else: 
                        sys.stdout.write(". ")
            sys.stdout.write("|")
            sys.stdout.write("\n")
        sys.stdout.write(" ")
        for i in range(self.width):
            sys.stdout.write("--")
        sys.stdout.write("\n")

    def get_transitions(self, state, direction):

        result = []
        x,y = state
        remain_p = 0.0

        if direction=="n": 
            success = (x,y-1)
            fail = [(x+1,y), (x-1,y)]
        elif direction=="s":
            success =  (x,y+1)
            fail = [(x+1,y), (x-1,y)]
        elif direction=="e":
            success = (x+1,y)
            fail= [(x,y-1), (x,y+1)]
        elif direction == "w":
            success = (x-1,y)
            fail= [(x,y-1), (x,y+1)]
          
        if success[0] < 0 or success[0] > self.width-1 or \
           success[1] < 0 or success[1] > self.height-1 or \
           success in self.blocked: 
                remain_p += self.success_prob
        else: 
            result.append((success, self.success_prob))
        
        for i,j in fail:
            if i < 0 or i > self.width-1 or \
               j < 0 or j > self.height-1 or \
               (i,j) in self.blocked: 
                    remain_p += self.fail_prob 
            else: 
                result.append(((i,j), self.fail_prob))
           
        if remain_p > 0.0: 
            result.append(((x,y), remain_p))
        return result

    def get_initial_utility_function(self):
        result = {}
        for x in range(self.width): 
            for y in range(self.height): 
                result[(x,y)] = 0.0
        return result

    #### Your code starts here ###
    
    def move(self, state, direction):
        """
        Return the state that results from going in this direction.
        """
        pos_moves = self.get_transitions(state, direction)
        r = random.random() #Gets decimal in between 0 to 1
        current_pro = 0
        for coordinate, probability in pos_moves:
            current_pro += probability
            if current_pro > r:
                return coordinate
        return 
    
    def get_random_policy(self):
        """
        Generate a random policy.
        """
        directions = ['n', 's', 'e', 'w']
        policy = {}
        
        
        for x in range(self.width):
            for y in range(self.height):
                    policy[(x,y)] = random.choice(directions)
        return policy # TODO

    def simple_policy_rollout(self, policy):
        """
        Return True if a random trial with this policy is successful.  
        """
        
        position = self.initial_state
        while True:
            position = self.move(position, policy[position])
            
            if position in self.targets:
                return True
            elif position in self.holes:
                return False
            else:
                return False
       

    def evaluate_policy(self, policy, t=100):
        """
        Return the percentage of successful trials within t random trials with
        this policy.  
        """
        complete = 0
        failure = 0
        
        for i in range(t):
            if self.simple_policy_rollout(policy):
                complete += 1
            else:
                failure += 1
        percentage = complete/(complete+failure)        
        
        return(percentage)
    
    def value_iteration(self, epsilon = 0.001):
        """
        The value iteration algorithm to iteratively compute an optimal
        utility function.
        """
        utility = self.get_initial_utility_function()
        
        best = False
        directions = ['n', 's', 'e', 'w']
        
        terminated = False 
        while not terminated:
            new_utility = self.get_initial_utility_function()
            terminated = True
            for x in range(self.width):
                for y in range(self.height):
                        state = (x, y)
                        reward = self.get_reward(state)
                        best_direction_sum = -math.inf
                        for direction in directions:
                            sum_total = 0
                            for (new_state, prob) in self.get_transitions(state, direction):
                                sum_total += prob * utility[new_state]
                            if sum_total > best_direction_sum:
                                best_direction_sum = sum_total
                        new_value = self.get_reward(state) + self.gamma * best_direction_sum
                        if abs(new_value - utility[state]) > (epsilon*(1-self.gamma)/self.gamma):
                             terminated = False
                        new_utility[state] = new_value 
            utility = new_utility 
        return utility

    def extract_policy(self, utility_function):
        """
        Given a utility function, return the best policy. 
        """
        
        
        return {} # 

if __name__ == "__main__":
   
    # Create a lake simulation 
    lake = FrozenLake(width=8,height=8, targets=[(3,4)], blocked = [(3,3),(2,3),(2,4), ], holes=[(4,0),(4,1),(3,0),(3,1), (6,4),(6,5),(0,7),(0,6),(1,7)], start=(0,0))
    
    policy = lake.get_random_policy()
    print(lake.evaluate_policy(policy))
    lake.print_map(policy)
    

    
