def getMinDiff(arr, n, k):
    arr.sort()
    result = arr[n - 1] - arr[0]
    for i in range(1, n):
        if arr[i] >= k:
            minE = min(arr[0] + k, arr[i] - k)
            maxE = max(arr[n - 1] - k, arr[i - 1] + k)
            result = min(result, maxE - minE)
    return result


if __name__ == "__main__":
    print(getMinDiff([1, 5, 8, 10], 4, 2))
