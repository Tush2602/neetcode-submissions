class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i,0) + 1
        maxm = None
        for ele, count in hash.items():
            if count > 1:
                return ele       
        