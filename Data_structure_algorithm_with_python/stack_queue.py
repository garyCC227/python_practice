'''
stack: LIFO -> last in first out

push() ->  push to top
pop() -> pull from top

应用：web browser back button, undo, 

Queue:FIFO -> First in first out

push() ->  push into back
pop() -> pull from front


'''

class Stack(object):
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]

    @property
    def size(self):
        return len(self.stack)


    def __str__(self):
        return ",".join(map(str,self.stack))

class Queue(object):
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    @property
    def size(self):
        return len(self.queue)

    def __str__(self):
        return ",".join(map(str,self.queue))



if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    print(queue)
    queue.dequeue()
    print(queue)
    queue.dequeue()
    print(queue)
