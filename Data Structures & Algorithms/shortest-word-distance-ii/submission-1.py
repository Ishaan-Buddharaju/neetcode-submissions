class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.idxMap = {} 
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word in self.idxMap:
                self.idxMap[word].append(i)
            else: 
                self.idxMap[word] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        res = float('inf')
        for pos1 in self.idxMap[word1]:
            for pos2 in self.idxMap[word2]:
                dist = abs(pos2 - pos1)
                if dist < res:
                    res = dist
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
