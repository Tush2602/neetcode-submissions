import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str =re.sub(r'[^A-Za-z0-9]', '', s).lower()
        n= len(clean_str)
        for i in range(n):
            if i < n/2 +1:
                if clean_str[i] != clean_str[n-1-i]:
                    return False
            else:
                break
        return True
        