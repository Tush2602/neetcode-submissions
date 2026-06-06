import numpy as np
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = nums.copy()
        for i in range(len(nums)):
            nums[i] = int(np.prod(np.array((a[:i] + a[i+1:]))))

        return list(nums)
        


        