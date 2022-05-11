def findLongestConseqSubseq(arr, N):
    arr.sort()
    size = 1
    maxSize = 1

    for index in range(1, N):
        if arr[index] == arr[index - 1] + 1:
            size += 1
        elif arr[index] != arr[index-1]:
            size = 1
        maxSize = max(maxSize, size)
    return maxSize


if __name__ == "__main__":
    #print(findLongestConseqSubseq([6, 6, 2, 3, 1, 4, 1, 5, 6, 2, 8, 7, 4, 2, 1, 3, 4, 5, 9, 6], 20))
    print(findLongestConseqSubseq([10, 20, 21, 22, 23], 5))
