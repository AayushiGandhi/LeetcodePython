#https://leetcode.com/problems/longest-substring-without-repeating-characters/
#https://www.youtube.com/watch?v=wiGpQwVHdE0&ab_channel=NeetCode
#Time complexity: O(n)
# Memory complexity: O(n)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        leftPointer = 0
        maxSize = 0
        charSet = set()

        for rightPointer in range(len(s)):
            while s[rightPointer] in charSet:
                charSet.remove(s[leftPointer])
                leftPointer += 1
            charSet.add(s[rightPointer])
            maxSize = max(maxSize, rightPointer - leftPointer + 1)

        return maxSize


