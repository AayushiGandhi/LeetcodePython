def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:
        return False

    rowLen, columnLen = len(matrix), len(matrix[0])
    start, end = 0, rowLen * columnLen - 1

    while start < end:
        mid = (start + end) // 2
        if matrix[mid // columnLen][mid % columnLen] < target:
            start = mid + 1
        else:
            end = mid
    return matrix[start // columnLen][start % columnLen] == target


if __name__ == "__main__":
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    print(searchMatrix(matrix, target))
