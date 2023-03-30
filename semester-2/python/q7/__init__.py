class BoundedStack:
    def __init__(self, maxlen):
        self.stack = []
        self.maxlen = maxlen

    def push(self, item):
        if len(self.stack) == self.maxlen:
            raise IndexError("Stack is full")
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def __len__(self):
        return len(self.stack)
