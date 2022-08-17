#Reason for using list of list for the table imstead pof a map is beacuse we want to iterate it in reverse order and map does not preserve order
#https://leetcode.com/problems/integer-to-roman/submissions/
#https://www.youtube.com/watch?v=ohBNdSJyLh8&ab_channel=NeetCode
7
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        symbolTable = [["I", 1], ["IV", 4], ["V", 5], ["IX", 9], ["X", 10], ["XL", 40], ["L", 50],
                       ["XC", 90], ["C", 100], ["CD", 400], ["D", 500], ["CM", 900], ["M", 1000]]

        for symbol, value in reversed(symbolTable):
            if num // value:
                count = num // value
                res += (symbol * count)
                num = num % value

        return res