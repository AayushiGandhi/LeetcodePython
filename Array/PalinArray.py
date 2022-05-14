def palinArray(arr, n):
    for i in arr:
        if str(i) != str(i)[::-1]:
            return 0
    return 1


if __name__ == "__main__":
    print(palinArray([111, 222, 333, 444, 555], 5))