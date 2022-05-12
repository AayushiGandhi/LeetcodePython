def binarySearch(a1, n, current):
    low = 0
    high = n - 1

    while low <= high:
        mid = (low + high) // 2
        if current == a1[mid]:
            return "Yes"
        if current < a1[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return "No"


def isSubsetBinary(a1, a2, n, m):
    a1.sort()

    if n < m:
        return "No"

    for i in a2:
        current = i
        ans = binarySearch(a1, n, current)
        if ans == "No":
            return "No"

    return ans


if __name__ == "__main__":
    print(isSubsetBinary([11, 1, 13, 21, 3, 7], [11, 3, 7, 1], 6, 4))
    print(isSubsetBinary([1, 2, 3, 4, 5, 6], [1, 2, 4], 6, 3))
    print(isSubsetBinary([10, 5, 2, 23, 19], [19, 5, 3], 5, 3))
