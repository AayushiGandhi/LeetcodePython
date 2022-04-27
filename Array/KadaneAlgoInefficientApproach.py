def max_sum_subarray(arr):
    res = []
    for i in range(len(arr)):
        temp = []
        for j in arr[i:]:
            temp.append(j)
            print(temp)
            res.append(sum(temp))

    print(res)
    return max(res)


if __name__ == "__main__":
    arr = [-1, -2, -3, -4]
    print(max_sum_subarray(arr))
