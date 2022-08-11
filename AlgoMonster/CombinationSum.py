#https://leetcode.com/problems/combination-sum/
#https://www.youtube.com/watch?v=qs1-iEla-5M&ab_channel=SaiAnishMalla

class Solution:
    def combinationSum(self, candidates, target: int):
        self.res = []
        self.candidates = candidates
        self.backtrack([], target, 0)
        return self.res

    def backtrack(self, path, target, index):
        if target == 0:
            self.res.append(path)
            return

        if target < 0:
            return

        for i in range(index, len(self.candidates)):
            self.backtrack(path + [self.candidates[i]], target - self.candidates[i], i)