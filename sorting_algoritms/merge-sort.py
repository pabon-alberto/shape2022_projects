# base case: if len(li)==1 return li done
# otherwise split the list into a left and right sublist of equal size.
# recursively sort each sublist.
# then merge the two sorted sublists together and return the result.

# For the merge step, implement a function def merge(left, right), that should merge the sorted lists left and right and return a new list. To merge, use an index a into the left sublist, and an index b into the right sublist. Compare the values at a and b, then write the smaller value to the result list and advance the corresponding index. 
# Continue until one of the indices reaches the end of its list. 
# Make sure to copy over any remaining entries from the other list

# Assume length of list is even for now.

from csv import list_dialects


def merge_sort(li):
    if len(li) == 1: return li
    else:
        list_a = []
        list_b = []
        list_c = [] #output this list
        half = len(li)//2

        list_a = li[0:half]
        list_b = li[half:]

        merge(list_a, list_b, list_c)

        return list_c
    
def merge(list_a, list_b, list_c): #todo *ALMOST FINISHED
    list_a.sort()
    list_b.sort()
    a = 0
    b = 0
    while a != len(list_a) or b != len(list_b):
        if list_a[a] < list_b[b] and a != len(list_a)-1:
            list_c.append(list_a[a])
            a += 1
        
        elif list_b[b] < list_a[a]:
            list_c.append(list_b[b])
            b += 1
            
        elif a == len(list_a)-1 and list_c[-1] != list_a[a]:
            list_c.append(list_a[a])
            list_c.append(list_b[b])
            return(list_c)

li = [2,1,3,4]
print(merge_sort(li))