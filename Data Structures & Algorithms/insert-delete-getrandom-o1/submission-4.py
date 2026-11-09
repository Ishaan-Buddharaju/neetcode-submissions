class RandomizedSet:

    def __init__(self):
        # self.myset = set()
        self.values = []
        self.lookup = {}
        self.Xn = 1759435
        self.a = 1664525
        self.c = 1013904223
        # pseudorandom: x_n = (aX_n-1 + c) mod m

    def insert(self, val: int) -> bool:
        # if not val in self.myset: 
        #     self.myset.add(val)
        #     return True
        # return False
        if not val in self.lookup:
            self.values.append(val)
            self.lookup[val] = len(self.values) - 1
            return True
        return False


    def remove(self, val: int) -> bool:
        # if val in self.myset: 
        #     self.myset.remove(val)
        #     return True
        # return False
        if val in self.lookup: 
            idx = self.lookup[val]
            last_element = self.values[-1]
            self.values[idx] = last_element
            self.lookup[last_element] = idx
            self.values.pop()
            del self.lookup[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)