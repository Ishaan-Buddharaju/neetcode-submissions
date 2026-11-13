class TimeMap:

    def __init__(self):
        self.timeMap = {}
        # self.minTime = float('inf')
        self.keyTimes = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[(key, timestamp)] = value
        if key in self.keyTimes: 
            self.keyTimes[key].append(timestamp)
        else: 
            self.keyTimes[key] = [timestamp]
        # hashed = ""
        # if timestamp < 1000: 
        #     hashed = key + str(timestamp)
        # else: 
        #     log = math.log(timestamp)
        #     offset = timestamp % (10 ** log)
        #     hashed = key + str(log) + str(offset)
        # self.timeMap[hasehed] = value
        
                

    def get(self, key: str, timestamp: int) -> str:
        if (key, timestamp) in self.timeMap: 
            return self.timeMap[(key, timestamp)]
        if key not in self.keyTimes:
            return ""
        
        searchtimes = self.keyTimes[key]
        l = 0
        r = len(searchtimes) - 1
        while (l <= r):
            m = (l + r) // 2
            val = searchtimes[m]
            if val <= timestamp: 
                l = m + 1
            else: 
                r = m - 1
        if r < 0: 
            return ""

        return self.timeMap[(key, searchtimes[r])]


        # hashed = ""
        # if timestamp < 1000: 
        #     hashed = key + str(timestamp)
        # else: 
        #     log = math.log(timestamp)
        #     offset = timestamp % (10 ** log)
        #     hashed = key + str(log) + str(offset)
        # return self.timeMap[hashed]