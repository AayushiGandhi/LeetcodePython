def rowWithMax1s(mat, R, C):
    max_row_index = 0
    index = C - 1

    for i in range(R):
        while index >= 0 and mat[i][index] == 1:
            index -= 1
            max_row_index = i
    if max_row_index == 0 and mat[0][C - 1] == 0:
        return -1

    return max_row_index


if __name__ == "__main__":
    mat = [[0, 0, 0, 0],
           [0, 1, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
    print("Index of row with maximum 1s is",
          rowWithMax1s(mat, 4, 4))