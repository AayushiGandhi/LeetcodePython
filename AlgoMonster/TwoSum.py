#https://www.youtube.com/watch?v=cQ1Oz4ckceM&ab_channel=NeetCode
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time complexity: O(n)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        leftPointer, rightPointer = 0, len(numbers) - 1

        while leftPointer < rightPointer:
            currentSum = numbers[leftPointer] + numbers[rightPointer]

            if currentSum > target:
                rightPointer -= 1
            elif currentSum < target:
                leftPointer += 1
            else:
                return [leftPointer + 1, rightPointer + 1]
        return []