class Queue:

    def __init__(self):
        self.queue = []
        self.len_queue = 0

    
    def push(self, e):
        self.queue.append(e)
        self.len_queue += 1


    def pop(self):
        if not self.empty():
            self.queue.pop(0)
            self.len_queue -= 1

    
    def empty(self):
        if self.len_queue == 0:
            return True
        return False


    def length(self):
        return self.len_queue


    def front(self):
        if not self.empty():
            return self.queue[0]


queue = Queue()
queue.push(5)
queue.push(3)
queue.push(8)
queue.pop()
queue.pop()
queue.pop()
print(queue.front())
print(queue.length())