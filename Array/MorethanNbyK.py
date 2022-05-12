def moreThanNdK(arr, n, k):
    map = {}
    result = []

    for index in range(n):
        if arr[index] in map.keys():
            map[arr[index]] += 1
            if map[arr[index]] > n//k and arr[index] not in result:
                result.append(arr[index])
        else:
            map[arr[index]] = 1

    return result


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
    print(moreThanNdK(arr, len(arr), 4))

    print("First Test")
    arr1 = [4, 5, 6, 7, 8, 4, 4]
    size = len(arr1)
    k = 3
    print(moreThanNdK(arr1, size, k))

    print("Second Test")
    arr2 = [4, 2, 2, 7]
    size = len(arr2)
    k = 3
    print(moreThanNdK(arr2, size, k))

    print("Third Test")
    arr3 = [2, 7, 2]
    size = len(arr3)
    k = 2
    print(moreThanNdK(arr3, size, k))

    print("Fourth Test")
    arr4 = [2, 3, 3, 2]
    size = len(arr4)
    k = 3
    print(moreThanNdK(arr4, size, k))

