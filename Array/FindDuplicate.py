#https://leetcode.com/problems/find-the-duplicate-number/

def findDuplicate(nums):
    d = {}
    for i in nums:
        if i in d.keys():
            return i
        else:
            d[i] = 0


if __name__ == "__main__":
    print(findDuplicate([1, 3, 4, 2, 2]))
