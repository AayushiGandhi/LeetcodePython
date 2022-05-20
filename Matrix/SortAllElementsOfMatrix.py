def sortedMatrix(N, Mat):
    arr = []
    for i in range(N):
        for j in range(N):
            arr.append(Mat[i][j])
    arr.sort()

    count = 0
    for i in range(N):
        for j in range(N):
            Mat[i][j] = arr[count]
            count += 1
    return Mat


if __name__ == "__main__":
    N = 4
    Mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    print(sortedMatrix(N, Mat))
