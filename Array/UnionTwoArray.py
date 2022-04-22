def union(a, b):
    return len(set(a) | set(b))


if __name__ == "__main__":
    arr1 = [1, 2, 3, 1, 2]
    arr2 = [1, 5, 6, 7, 2]
    print(union(arr1, arr2))
