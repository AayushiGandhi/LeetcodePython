def inversionCount(arr, n):
    if n == 0:
        return 0
    count = 0
    flag = True
    while flag:
        flag = False
        previous = 0
        for next in range(1, n):
            if arr[previous] > arr[next]:
                count += 1
                arr[previous], arr[next] = arr[next], arr[previous]
                flag = True
            previous = next
    return count


if __name__ == "__main__":
    print(inversionCount([1, 20, 6, 4, 5], 5))