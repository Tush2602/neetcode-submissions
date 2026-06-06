class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n= len(nums)
        op = [1] *n

        p =1
        for i in range(n):
            op[i] =p
            p = p*nums[i]
        
        s=1
        for i in range(n-1, -1, -1):
            op[i] = op[i] * s
            s = s * nums[i]

        return op

