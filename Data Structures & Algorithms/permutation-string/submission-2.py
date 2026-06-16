class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = {}
        window = {}
        
        for c in s1:
            s1_count[c] = s1_count.get(c, 0) + 1
        
        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            l = r - len(s1) + 1
            if r >= len(s1):
                left_char = s2[r - len(s1)]
                window[left_char] -= 1
                if window[left_char] == 0:
                    del window[left_char]
            
            if window == s1_count:
                return True
        
        return False