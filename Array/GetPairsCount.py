def getPairsCount(arr, n, k):
    map = {}
    count = 0
    for i in arr:
        current = k - i
        if current in map.keys():
            count += map[current]

        if i in map:
            map[i] += 1
        else:
            map[i] = 1
    return count


if __name__ == "__main__":
    print(getPairsCount([1, 5, 7, 1], 4, 6))
