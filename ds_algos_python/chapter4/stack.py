class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            False

    def size(self):
        return len(self.items)

    def peek_all(self):
        return self.items
