class Stack:
    def __init__(self, max_size):
        self.stack = []
        self.max_size = max_size

    def push(self, element):
        if len(self.stack) >= self.max_size:
            raise OverflowError("Stack Overflow: Cannot push element, stack is full.")
        self.stack.append(element)

    def pop(self):
        if self.isempty():
            raise IndexError("Stack Underflow: Cannot pop element, stack is empty.")
        return self.stack.pop()

    def isempty(self):
        return len(self.stack) == 0

    def top(self):
        if self.isempty():
            raise IndexError("Stack is empty: No top element.")
        return self.stack[-1]