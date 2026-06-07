class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        k = 0
        left, right = k + 1, len(nums) - 1
        output = []

        while k < len(nums) - 2:

            if nums[left] + nums[right] > -nums[k]:
                right -= 1

            elif nums[left] + nums[right] < -nums[k]:
                left += 1

            else:
                if [nums[k], nums[left], nums[right]] not in output:
                    output.append([nums[k], nums[left], nums[right]])

                left += 1
                right -= 1

            if left >= right:
                k += 1
                left = k + 1
                right = len(nums) - 1

        return output