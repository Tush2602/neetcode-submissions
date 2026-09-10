
class Solution:
    def partition(self, s: str):
        res = []
        part = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(i):
            # We have partitioned the entire string
            if i == len(s):
                res.append(part.copy())
                return

            # Try every possible substring starting at i
            for j in range(i, len(s)):
                # Only choose palindrome substrings
                if isPalindrome(i, j):
                    part.append(s[i:j + 1])

                    # Solve the remaining string
                    backtrack(j + 1)

                    # Undo the choice
                    part.pop()

        backtrack(0)
        return res

