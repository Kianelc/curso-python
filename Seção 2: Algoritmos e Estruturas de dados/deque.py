class Deque():

    def __init__(self):
        self.deque = []
        self.len_deque = 0


    def empty(self):
        if self.len_deque == 0:
            return True
        return False


    def push_front(self, e):
        self.deque.insert(0, e)
        self.len_deque += 1


    def push_back(self, e):
        self.deque.insert(self.len_deque, e)
        self.len_deque += 1


    def pop_front(self):
        if not self.empty():
            self.deque.pop(0)
            self.len_deque -= 1


    def pop_back(self):
        if not self.empty():
            self.deque.pop(self.len_deque - 1)
            self.len_deque -= 1


    def front(self):
        if not self.empty():
            return self.deque[0]


    def back(self):
        if not self.empty():
            return self.deque[-1]

    
    def show(self):
        for i in self.deque:
            print(i, end=' ')


deque = Deque()

# Teste de Inserção
deque.push_front(10) # 10
deque.push_front(5) # 5 > 10
deque.push_back(20) # 5 > 10 > 20
deque.push_front(7) # 7 > 5 > 10 > 20
deque.push_back(40) # 7 > 5 > 10 > 20 > 40
deque.show()
print('\nFront: %d' % deque.front())
print('Back: %d' % deque.back())

deque.pop_back() # 7 > 5 > 10 > 20
deque.show()
print('\n')
deque.pop_front() # 5 > 10 > 20
deque.show()
print('\n')

