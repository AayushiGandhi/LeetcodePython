def findMinDiff(arr,n,m):
    arr.sort()
    minDiff = arr[n - 1] - arr[0]
    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if minDiff > diff:
            minDiff = diff

    return minDiff


if __name__ == "__main__":
    arr = "87 78 16 94 36 87 93 50 22 63 28 91 60 64 27 41 27 73 37 12 69 68 30 83 31 63 24 68 36 30 3 23 59 70 68 94 57 12 43 30 74 22 20 85 38 99 25 16 71 14 27 92 81 57 74 63 71 97 82 6 26 85 28 37 6 47 30 14 58 25 96 83 46 15 68 35 65 44 51 88 9 77 79 89"
    arr1 = list(map(int,arr.split()))
    print(findMinDiff(arr1, len(arr1), 61))