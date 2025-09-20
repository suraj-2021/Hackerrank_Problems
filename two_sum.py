class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            y = target - nums[i]
            if y in nums and nums.index(y) != i:
                return [i, nums.index(y)]
