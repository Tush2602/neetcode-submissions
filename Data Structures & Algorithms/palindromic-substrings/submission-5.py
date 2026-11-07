class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = {}
        n = len(s)
        cnt = 0
        dp = [[False] * n for _ in range(n)] 

        #length1
        for i in range(n):
            dp[i][i] = True
            cnt+=1
        
        #length2
        for i in range(n-1):
            if s[i] == s[i+1]:
                cnt+=1
                dp[i][i+1]= True

        #length3 
        for length in range(3, n+1):
            for i in range(n-length+1):
                j = i+length - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    cnt+=1
                    dp[i][j] = True

        return cnt

