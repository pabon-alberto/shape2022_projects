#Not finished
#Stack: Last in, first out
#Queue: First in, first out
#Heap: First in, best out

#Heap order property: all the children must have a greater value than its parent.

from math import floor

# li = [3,6,1,5,9,8]
li = [1,2,3,4,5,6]

def heappush(li, x):
    li.append(x)
    status = True
    index = len(li) - 1

    while status == True:
        parent = index//2

        if x < li[parent]:
            li[index] = li[parent]
            li[parent] = x
            index = parent
        else:
            status = False

    return(li)
    # for i in range(len(li), -1, -1):
    #     parent = li[i//2]
    #     left_node = li[(2*i)+1]
    #     right_node = li[(2*i)+2]

    #     li.append(x)
    #     if 

    return

def heappop(li):
    return(li.pop())


def heapify(li): #i is index
    least = min(li)
    first = li[0] #4

    least, first = first, least
    i, j = li.index(least), li.index(first)

    li[i], li[j] = li[j], li[i]
    return(li)

# heappush(li, 2)
# heappush(li, 5)
# heappush(li, 3)
print(heappush(li, 2))







