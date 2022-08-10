#https://leetcode.com/problems/maximum-average-pass-ratio/
#https://www.youtube.com/watch?v=ZjydWQCVg80&t=471s&ab_channel=HappyCoding
#classes=n, extraStudents=m
#Time complexity: O(n+mlogn)
#Memory complexity: O(n)

import heapq


class Solution:
    def maxAverageRatio(self, classes, extraStudents):

        priorityQueue = []

        for passed, total in classes:
            heapq.heappush(priorityQueue, ((passed / total - (passed + 1) / (total + 1)), passed, total))

        while extraStudents > 0:
            _, passed, total = heapq.heappop(priorityQueue)
            passed += 1
            total += 1
            heapq.heappush(priorityQueue, ((passed / total - (passed + 1) / (total + 1)), passed, total))
            extraStudents -= 1

        return sum([passed / total for _, passed, total in priorityQueue]) / len(classes)