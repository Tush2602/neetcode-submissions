
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        k = 0
        left, right = k + 1, len(nums) - 1
        output = []

        while k < len(nums) - 2:
            
            if k>0 and nums[k] == nums[k-1]:
                k+=1
                left, right = k+1, len(nums)-1
                continue

            if nums[left] + nums[right] > -nums[k]:
                right -= 1

            elif nums[left] + nums[right] < -nums[k]:
                left += 1

            else:
                output.append([nums[k], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1

                left += 1
                right -= 1

            if left >= right:
                k += 1
                left = k + 1
                right = len(nums) - 1

        return output
