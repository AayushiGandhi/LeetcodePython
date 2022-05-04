def minJumps( arr, n):
    # code here
    index = 0
    element = arr[0]
    count = 0

    if n == 1:
        return 0

    while index + element + 1 < n:
        if element == 0:
            return -1
        updatedArr = arr[index + 1: index + element + 1]
        maxi = 0
        for j in updatedArr:
            maxiIndex = updatedArr.index(j) + j
            if maxi <= maxiIndex:
                maxi = maxiIndex
                element = j

        index += updatedArr.index(element) + 1
        count += 1
    return count + 1


if __name__ == "__main__":
    print(minJumps([2, 1, 0, 3],4))