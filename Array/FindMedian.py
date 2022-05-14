def find_median(v):
    v.sort()
    length = len(v)

    if length % 2 == 0:
        return (v[length // 2 - 1] + v[length // 2]) // 2
    else:
        return v[length // 2]


if __name__ == "__main__":
    print(find_median([90, 100, 78, 89, 67]))