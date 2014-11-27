class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak(self, s, dict):
        if not s or not dict: return False
        if s in dict : return True
        return self.dpCheck(s,dict)

    def wordBreak2(self, s, dict):
        if not s or not dict: return []
        if s in dict : return [s]
        Solution.results = []
        self.dfs(s, dict, '')
        return Solution.results


    def dfs(self, s, dict, result):
        if self.dpCheck(s, dict):
            # if the s is end , put result to results
            if len(s) == 0: Solution.results.append(result[1:])
            for i in range(1, len(s)+1):
                if s[:i] in dict:
                    self.dfs(s[i:], dict, result+' '+s[:i])

    def dpCheck(self, s, dict):
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        for i in range(1, len(s)+1):
            for k in range(i):
                if dp[k] and s[k:i] in dict:
                    dp[i] = True
        return dp[len(s)]

if __name__ == '__main__':
    so = Solution()
    print so.wordBreak2("ab",["a","b"])