class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if hash.get(num, 0):
                hash[num]+=1
            else:
                hash[num] = 1
        return list(dict(sorted(hash.items(), key=lambda x:x[1], reverse=True)).keys())[:k]