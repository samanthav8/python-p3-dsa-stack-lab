class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.full():
            raise Exception("Stack is full")
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None  # Change to return None if stack is empty
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            # Reverse the list to count from the top
            index_from_top = self.items[::-1].index(target)
            return index_from_top
        except ValueError:
            return -1
