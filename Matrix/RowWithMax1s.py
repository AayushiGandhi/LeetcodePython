def rowWithMax1s():
    leftMostIndex = -1
    maxRowIndex = m
    for index in range(m - 1, -1, -1):
        if arr[0][index] == 1:
            maxRowIndex = arr[0][index]

    for rowIndex in range(1, n):
        if arr[rowIndex][leftMostIndex - 1] == 1:
            while arr[rowIndex][leftMostIndex - 1] != 0:
                leftMostIndex -= 1
            leftMostIndex -= 1
            maxRowIndex = rowIndex

    return maxRowIndex


if __name__ == "__main__":
    arr = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
    n = 3
    m = 9
    print(rowWithMax1s())
