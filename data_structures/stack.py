class Stack:
    def __init__(self):
        self.queue = []

    def empty(self):
        return self.top() is None

    def push(self, value) -> None:
        self.queue.append(value)

    def top(self):
        try:
            return self.queue[-1]
        except IndexError as ie:
            return None

    def pop(self):
        try:
            top_value = self.queue[-1]
            self.queue.pop()
            return top_value

        except IndexError:
            return None













