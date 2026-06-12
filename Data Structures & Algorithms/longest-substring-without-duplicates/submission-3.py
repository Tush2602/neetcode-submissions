class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        window =set()
        size=0
        l, r = 0, 0
        while r<n:
            if s[r] not in window:
                window.add(s[r])
                size= max(size, r-l+1)
                r+=1
            else:
                window.remove(s[l])
                l+=1
        return size