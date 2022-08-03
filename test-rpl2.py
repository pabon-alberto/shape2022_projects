ex = [3, '+', 2,'*', 5] #3 2 5 * +
stack = []


less_im = 0
more_im = 0

for i in range((len(ex)-1), -1, -1):
    if isinstance(ex[i], int) == True:
        stack.append(ex[i])

    #elif (isinstance(ex[i], int) == False):
        #if ex[i] == '*' or ex[i] == '/':


    if ex[0] == stack[-1]:
        j = 0
        for j in ex:
            if isinstance(j, int) == False:
                stack.append(j)
print(stack)
