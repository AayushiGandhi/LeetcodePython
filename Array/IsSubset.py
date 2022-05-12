def isSubset(a1, a2, n, m):
    for i in a2:
        if i not in a1:
            return "No"
    return "Yes"


if __name__ == "__main__":
    print(isSubset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1], 6, 4))
    print(isSubset([1, 2, 3, 4, 5, 6], [1, 2, 4], 6, 3))
    print(isSubset([10, 5, 2, 23, 19], [19, 5, 3], 5, 3))
