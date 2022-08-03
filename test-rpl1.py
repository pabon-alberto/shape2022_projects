rpl = [2,3,4,'*', '+']
def evaluate(rpl):
    stack = []
    for i in range(len(rpl)): #This makes i a pointer, if it was for i in range(rpl), i would contain the value at that index.
        if rpl[i] == '+':
            sum_result = rpl[i-2] + rpl[i-1]
            for i in range(3): 
                rpl.pop(1)
            stack.append(sum_result)
        if rpl[i] == '-':
            sub_result = rpl[i-2] - rpl[i-1]
            for i in range(3):
                rpl.pop(1)
            stack.append(sub_result)
        if rpl[i] == '*':
            mul_result = rpl[i-2] * rpl[i-1]
            for i in range(3):
                rpl.pop(1)
            stack.append(mul_result)
        if rpl[i] == '/':
            mul_result = rpl[i-2] / rpl[i-1]
            for i in range(3):
                rpl.pop(1)
            stack.append(mul_result)
    
    return(stack.pop())
print(evaluate(rpl))