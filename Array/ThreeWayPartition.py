def threeWayPartition(array, a, b):
    n = len(array)
    start = 0
    end = n - 1
    i = 0

    while i <= end:
        if array[i] < a:
            array[i], array[start] = array[start], array[i]
            start += 1
            i += 1
        elif array[i] > b:
            array[i], array[end] = array[end], array[i]
            end -= 1
        else:
            i += 1

    return array


if __name__ == "__main__":
    print(threeWayPartition([1, 2, 3, 3, 4], 1, 2))