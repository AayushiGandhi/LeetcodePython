#https://leetcode.com/problems/reorder-data-in-log-files/
#https://www.youtube.com/watch?v=Ie7VMpZlLrY&t=258s&ab_channel=thecodingworld
class Solution:
    def reorderLogFiles(self, logs):
        alpha, digit = [], []

        for log in logs:
            if (log.split()[1].isdigit()):
                digit.append(log)
            else:
                alpha.append(log.split())

        alpha.sort(key=lambda x: x[0])
        alpha.sort(key=lambda x: x[1:])

        for i in range(len(alpha)):
            alpha[i] = (" ".join(alpha[i]))

        alpha.extend(digit)
        return alpha