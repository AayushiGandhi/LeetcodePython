def spirallyTraverse(matrix, r, c):
    rowStart = 0
    rowEnd = r
    columnStart = 0
    columnEnd = c
    ans = []

    while rowStart < rowEnd and columnStart < columnEnd:

        # first row
        for columnIndex in range(columnStart, columnEnd):
            ans.append(matrix[rowStart][columnIndex])
        rowStart += 1

        # last column
        for rowIndex in range(rowStart, rowEnd):
            ans.append(matrix[rowIndex][columnEnd-1])
        columnEnd -= 1

        # last row
        if rowStart < rowEnd:
            for columnIndex in range(columnEnd-1, columnStart-1, -1):
                ans.append(matrix[rowEnd-1][columnIndex])
            rowEnd -= 1

        # first column
        if columnStart < columnEnd:
            for rowIndex in range(rowEnd-1, rowStart-1, -1):
                ans.append(matrix[rowIndex][columnStart])
            columnStart += 1

    return ans


if __name__ == "__main__":
    a = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

    R = 4
    C = 4
    print(spirallyTraverse(a, R, C))