# https://leetcode.com/problems/two-sum/submissions/
#https://leetcode.com/problems/two-sum/discuss/1378064/C%2B%2BJavaPython-HashMap-Two-pointers-Solutions-Clean-and-Concise
#Time: O(N)
#Space: O(N)

class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for index, b in enumerate(nums):
            a = target - b

            if a in seen:
                return [seen[a], index]

            seen[b] = index
