from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = nums.copy()
        for i in range(len(nums)):
            nums[i] = math.prod(a[:i] + a[i+1:])

        return list(nums)
        