def max_sum_subarray(arr):
    max = arr[0]
    sum = 0
    for i in arr:
        if sum + i > max:
            max = sum + i
        if sum + i <= 0:
            sum = 0
        else:
            sum = sum + i

    return max


if __name__ == "__main__":
    arr = [-81, -71, 98, 55, 76, -52, 68, 15, -77, 77, -42, -70, -53, 86, 29, -30, 14, 25, -94, 73, -68, 81, 44]
    print(max_sum_subarray(arr))
