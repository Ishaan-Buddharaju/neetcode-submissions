class MinStack:

    def __init__(self):
        self.values = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.values.append(val)
        if len(self.minimum) == 0 or self.minimum[-1] >= val:
            self.minimum.append(val)
        
    def pop(self) -> None:
        res = self.values.pop()
        if res == self.minimum[-1]:
            self.minimum.pop()
    def top(self) -> int:
        # never called on empty
        return self.values[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
