def countSmallerThanEqualToMid(row, mid):
    low = 0
    high = len(row) - 1

    while low <= high:
        m = (low + high) // 2
        if row[m] <= mid:
            low = m + 1
        else:
            high = m - 1

    return low


def binaryMedian(m, rowLen, columnLen):
    low = 0
    high = 10**9

    for i in range(r):
        if m[i][0] < low:
            low = m[i][0]
        if m[i][d - 1] > high:
            high = m[i][d - 1]

    while low <= high:
        mid = (low + high) // 2
        count = 0

        for i in range(rowLen):
            count += countSmallerThanEqualToMid(m[i], mid)

        if count <= (rowLen * columnLen) // 2:
            low = mid + 1
        else:
            high = mid - 1

    return low


if __name__ == "__main__":
    r, d = 3, 3
    m = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    print(binaryMedian(m, r, d))
