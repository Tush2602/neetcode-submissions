class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l, r = 0,0
        size = 0
        while r<n:
            if s[r] not in s[l:r]:
                size= max(size, r-l+1)
                r+=1
            else:
                l+=1

        return size