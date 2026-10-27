class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 : 
            return 0
        temp1= 0
        temp2 = nums[0]
        for i in range(2, n+1):
            take = nums[i-1] + temp1
            skip= temp2
            temp1 = temp2
            temp2 = max(take, skip)

        return temp2