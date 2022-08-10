#https://leetcode.com/problems/k-closest-points-to-origin/submissions/
#https://www.youtube.com/watch?v=rI2EBUEMfTk&t=114s&ab_channel=NeetCode
#Time complexity: O(n)

import heapq


class Solution:
    def kClosest(self, points, k):
        distance = []
        res = []

        for x, y in points:
            distance.append([(x ** 2) + (y ** 2), x, y])

        heapq.heapify(distance)

        while k > 0:
            dis, x, y = heapq.heappop(distance)
            res.append([x, y])
            k -= 1

        return res