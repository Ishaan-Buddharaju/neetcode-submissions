class Solution:
    def numDecodings(self, s: str) -> int:

        self.memo = {}

        def dfs(i):
            if i == len(s):
                self.memo[i] = 1
                return

            if s[i] == "0":
                self.memo[i] = 0
                return

            if i in self.memo:
                return

            # Single-digit decision
            dfs(i + 1)
            self.memo[i] = self.memo[i + 1]

            # Double-digit decision
            if i + 1 < len(s):
                num = int(s[i:i + 2])

                if 10 <= num <= 26:
                    dfs(i + 2)
                    self.memo[i] += self.memo[i + 2]

        dfs(0)
        return self.memo[0]