def subArrayExists(arr, n):
    sum = 0
    s = set()

    for index in range(n):
        sum += arr[index]

        if sum == 0 or sum in s:
            return True
        s.add(sum)
    return False


if __name__ == "__main__":
    print(subArrayExists([0, 9, 7, -12, 5], 5))