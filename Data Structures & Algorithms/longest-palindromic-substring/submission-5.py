class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res_start, res_len = 0, 1
        
        #length 1 
        for i in range(n):
            dp[i][i] = True
        
        #length 2 
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                res_start, res_len = i, 2

        #length 3 
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = length + i -1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] =True
                    res_start, res_len = i, length

        return s[res_start:res_start+res_len]