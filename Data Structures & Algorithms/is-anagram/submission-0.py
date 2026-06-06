class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        t = list(t)
        for i in s:
            if i in t:
                t.remove(i)
            else:
                return False
        return True
        