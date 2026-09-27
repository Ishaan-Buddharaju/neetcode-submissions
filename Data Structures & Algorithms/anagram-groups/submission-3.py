class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort and append
        # result = defaultdict(list)
        # for s in strs: 
        #     key = str(sorted(s))
        #     result[key].append("" + s)
       
        # return list(result.values())

        '''
        Since every freq map must match we can use it to append to      
        result while removing the linearithmic sorting operation
        '''

        result = defaultdict(list)
        for s in strs:
            freqMap = [0] * 26
            for char in s: 
                freqMap[ord(char) - 97] += 1
            result[tuple(freqMap)].append("" + s)
            freqMap = [0] * 26

        return list(result.values())



