#https://leetcode.com/problems/merge-intervals/
#https://www.youtube.com/watch?v=44H3cEC2fFM&ab_channel=NeetCode
#O(nlogn)
class Solution:
    def merge(self, intervals):

        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start, end])

        return output