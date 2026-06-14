class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}
        l = 0 
        size = 0
        for r in range(len(s)):
            hash[s[r]] = hash.get(s[r], 0) + 1
            while (r-l+1) - max(hash.values())> k:
                hash[s[l]]-=1
                l+=1
            size = max(size, r-l+1)

        return size 