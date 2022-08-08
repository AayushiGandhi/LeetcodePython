#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
#https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
# Time complexity: O(N)


def numPairsDivisibleBy60(time):
    hash = {}
    totalPairs = 0

    for num in time:
        modNum = num % 60

        if modNum == 0:
            if 0 in hash:
                totalPairs += hash[0]
        elif (60 - modNum) in hash:
            totalPairs += hash[60 - modNum]

        if modNum in hash:
            hash[modNum] += 1
        else:
            hash[modNum] = 1

    return totalPairs

time = [30,20,150,100,40]
print(numPairsDivisibleBy60(time))