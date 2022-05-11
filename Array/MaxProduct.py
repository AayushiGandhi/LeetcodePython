def maxProduct(arr, n):
    minVal = arr[0]
    maxVal = arr[0]
    maxProduct = arr[0]

    for i in range(1, n):
        # When multiplied by -ve number, maxVal becomes minVal and minVal becomes maxVal.
        if (arr[i] < 0):
            minVal, maxVal = maxVal, minVal

        # maxVal and minVal stores the product of subarray ending at arr[i].
        maxVal = max(arr[i], maxVal * arr[i])
        minVal = min(arr[i], minVal * arr[i])

        maxProduct = max(maxProduct, maxVal)

    return maxProduct


if __name__ == "__main__":
    print(maxProduct([-1, -3, -10, 0, 60], 5))