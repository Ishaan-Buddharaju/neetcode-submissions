class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i >= len(s):
                return True
            if i in memo:
                return memo[i]

            for word in wordDict: 
                match = True
                for j in range(len(word)):
                    if i + j >= len(s) or s[i + j] != word[j]:
                        match = False
                        break
                
                if match: 
                    result = dfs(i + len(word))
                    if result:
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return dfs(0)
        
                
            