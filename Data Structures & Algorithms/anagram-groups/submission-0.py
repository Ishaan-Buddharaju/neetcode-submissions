class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        copy = []
        for i in range(len(strs)):
            sortedString = ''.join(sorted(strs[i]))
            copy.append((sortedString, i))
        copy.sort(key = lambda word: word[0])
        output = []
        i = 0
        j = 0
        while True:
            anagrams = []
            while j != len(copy): 
                if copy[i][0] == copy[j][0]:
                    anagrams.append(strs[copy[j][1]])
                    j += 1
                else: 
                    i = j
                    break
            output.append(anagrams)
            if j == len(copy): 
                break
            anagrams = []


        return output

