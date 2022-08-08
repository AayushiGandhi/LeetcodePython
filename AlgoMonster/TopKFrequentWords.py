#https://leetcode.com/problems/top-k-frequent-words/
#https://www.youtube.com/watch?v=96hCN6t6rDg&ab_channel=babybear4812

import heapq


class Solution:
    def topKFrequent(self, words, k):
        # create dict
        map = {}
        for word in words:
            if word in map:
                map[word] += 1
            else:
                map[word] = 1

        # create heap
        heap = [(-freq, word) for word, freq in map.items()]
        heapq.heapify(heap)

        # return top k most frequent words
        return [heapq.heappop(heap)[1] for _ in range(k)]
