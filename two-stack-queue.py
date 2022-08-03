class TwoStackQueue:
    def __init__(self):
        self.instack = [] #add an item to this stack
        self.outstack = [] #pop on item out of this stack

    def enqueue(self, item):
        self.instack.append(item)
        return

    def dequeue(self):
        if self.instack: #If not empty
            for i in range(len(self.instack)):
                self.outstack.append(self.instack.pop())
            return(self.outstack.pop())
        else:
            return(self.outstack.pop())

q = TwoStackQueue()

q.enqueue("C")
q.enqueue(2)
q.enqueue("A")
q.enqueue('2')


print(q.dequeue()) # print C
print(q.dequeue()) # print 2
print(q.dequeue()) # print A
print(q.dequeue()) 