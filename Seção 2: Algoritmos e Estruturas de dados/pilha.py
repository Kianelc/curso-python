class Stack:

    def __init__(self):
        self.stack = []
        self.len_stack = 0


    def push(self, e):
        self.stack.append(e)
        self.len_stack += 1


    def pop(self):
        if not self.empty():
            self.stack.pop(self.len_stack - 1)
            self.len_stack -= 1

    
    def top(self):
        if not self.empty():
            return self.stack[-1]
        None


    def empty(self):
        if self.len_stack == 0:
            return True
        return False


    def length(self):
        return self.len_stack


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print('Topo da lista', stack.top())
print('A pilha está vazia: ', stack.empty())
print('Tamanho da lista: ', stack.length())
stack.pop()
print('Topo da lista', stack.top())
stack.pop()
print('Topo da lista', stack.top())
print('Tamanho da lista: ', stack.length())
stack.pop()
print('Topo da lista', stack.top())