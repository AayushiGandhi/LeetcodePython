#https://leetcode.com/problems/median-of-two-sorted-arrays/
#https://www.youtube.com/watch?v=q6IEA26hvXc&t=1119s&ab_channel=NeetCode
#Time : O(log(min(n, m)))

class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float:
        total = len(num1) + len(num2)
        half = total // 2

        if len(num1) > len(num2):
            num1, num2 = num2, num1

        l, r = 0, len(num1) - 1
        while True:
            i = (l + r) // 2  # middle of num1
            j = half - i - 2  # middle of num2

            Aleft = num1[i] if i >= 0 else float("-infinity")
            Aright = num1[i + 1] if i + 1 < len(num1) else float("+infinity")
            Bleft = num2[j] if j >= 0 else float("-infinity")
            Bright = num2[j + 1] if j + 1 < len(num2) else float("+infinity")

            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1