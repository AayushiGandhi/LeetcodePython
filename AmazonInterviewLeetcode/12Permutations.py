# Backtracking builds potential candidates to solution and abandons a candidate if it no longer leads to a valid solution
# - this is also called pruning the recursion tree.
#https://leetcode.com/problems/permutations/
#https://www.youtube.com/watch?v=s7AvT7cGdSo&ab_channel=NeetCode

class Solution:
    def permute(self, nums):
        result = []

        if (len(nums) == 1):
            return [nums[:]]

        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            result.extend(perms)
            nums.append(n)
        return result

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))
