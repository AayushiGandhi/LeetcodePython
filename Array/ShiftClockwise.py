def shiftClockwise(arr):
    arr.insert(0, arr[-1])
    del arr[-1]
    return arr


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, -44, 5, 6, -7, 8, 9]
    print(shiftClockwise(arr))
