class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort and append
        result = defaultdict(list)
        for s in strs: 
            key = str(sorted(s))
            result[key].append("" + s)
       
        return list(result.values())

