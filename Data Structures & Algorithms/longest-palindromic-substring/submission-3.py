class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        memo = {}
        res_start, res_len = 0,0

        def is_pal(l, r):
            if l >= r :
                return True
            if (l, r) in memo:
                return memo[(l,r)]
            memo[(l,r)] = s[l] == s[r] and is_pal(l+1, r-1)
            return memo[(l,r)]
        
        for i in range(n):
            for j in range(i, n):
                if j-i+1 > res_len and is_pal(i,j):
                    res_start, res_len = i, j-i+1

        return s[res_start:res_start + res_len]