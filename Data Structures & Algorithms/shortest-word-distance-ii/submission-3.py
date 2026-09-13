class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.idxMap = {} 
        for i in range(len(wordsDict)):
            word = wordsDict[i]
            if word in self.idxMap:
                self.idxMap[word].append(i)
            else: 
                self.idxMap[word] = [i]

        # runtime O(n) space O(n)

    def shortest(self, word1: str, word2: str) -> int:
        # res = float('inf')
        # for pos1 in self.idxMap[word1]:
        #     for pos2 in self.idxMap[word2]:
        #         dist = abs(pos2 - pos1)
        #         if dist < res:
        #             res = dist
        # return res

        # # runtime O(n^2) and space O(1)

        # USE two pointers to avoid the divergent pos checks

        res = float('inf')
        p1, p2 = 0, 0
        pos1 = self.idxMap[word1]
        pos2 = self.idxMap[word2]
        while p1 < len(pos1) and p2 < len(pos2):
            idx1, idx2 = pos1[p1], pos2[p2]
            dist = abs(pos1[p1] - pos2[p2])
            if dist < res:
                res = dist
            if idx1 < idx2:
                p1 += 1
            else:
                p2 += 1
            
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
