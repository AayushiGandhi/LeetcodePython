# https://leetcode.com/problems/two-sum/submissions/

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for index, b in enumerate(nums):
            a = target - b

            if a in seen:
                return [seen[a], index]

            seen[b] = index
