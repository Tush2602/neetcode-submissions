class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = {}
        for i in strs:
            sr= ''.join(sorted(i))
            if hash.get(sr, 0):
                hash[sr].append(i)
            else:
                hash[sr] = [i]
        return [v for v in hash.values()]
        