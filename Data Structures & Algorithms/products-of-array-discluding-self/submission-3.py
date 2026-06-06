from math import prod
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1] * len(nums)

        p =1
        for i in range(len(nums)):
            op[i] =p
            p = p*nums[i]
        
        s=1
        for i in range(len(nums)-1, -1, -1):
            op[i] = op[i] * s
            s = s * nums[i]

        return op

