class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a = nums.copy()
        for i in range(len(nums)):
            b = 1
            for j in range(len(nums)):
                if i==j:
                    continue
                b = b * a[j]
            nums[i] = b 
        return nums


        