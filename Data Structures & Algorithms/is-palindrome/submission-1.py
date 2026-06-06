class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str =''.join([sub for sub in s if sub.isalnum()]).lower()
        n= len(clean_str)
        for i in range(n):
            if i < n/2 +1:
                if clean_str[i] != clean_str[n-1-i]:
                    return False
            else:
                break
        return True
        