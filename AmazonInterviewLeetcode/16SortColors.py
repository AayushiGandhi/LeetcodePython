#Sort color could be solved with the help of bucket sort however, bucket sort requires 2 passes of whole array
#Therefore, we use quick sort which only requires single pass
#https://leetcode.com/problems/sort-colors/submissions/
#https://www.youtube.com/watch?v=4xbWSRZHqac&ab_channel=NeetCode

class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0

        while i <= r:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i += 1

            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1

            else:
                i += 1