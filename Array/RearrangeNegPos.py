def rearrange(arr):
    res = []
    for i in arr:
        if i < 0:
            res.append(i)
            arr.remove(i)
    return res + arr


if __name__ == "__main__":
    arr = [-1, 2, -3, 4, -44, 5, 6, -7, 8, 9]
    print(rearrange(arr))
