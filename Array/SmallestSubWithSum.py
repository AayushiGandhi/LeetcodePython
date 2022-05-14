def smallestSubWithSum(a, n, x):
    currentTotal = 0
    minLen = n + 1
    start = 0
    end = 0

    while end < n:

        while currentTotal <= x and end < n:
            currentTotal += a[end]
            end += 1

        while currentTotal > x and start < n:
            if end - start < minLen:
                minLen = end - start
            currentTotal -= a[start]
            start += 1

    return minLen


if __name__ == "__main__":
    print(smallestSubWithSum([1, 10, 5, 2, 7], 5, 9))