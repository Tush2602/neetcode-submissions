class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        di = dict()
        for i in nums:
            if di.get(i, 0):
                return True

            di[i]= 1

        return False