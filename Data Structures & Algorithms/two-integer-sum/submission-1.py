class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = dict()
        for i in range(len(nums)):
            rem= target - nums[i]
            if hash.get(rem, 0):
                return [hash[rem]-1, i]
            hash[nums[i]] = i+1 