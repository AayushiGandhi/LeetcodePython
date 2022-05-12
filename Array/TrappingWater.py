def trappingWater(arr, n):
    leftIndex = 0
    rightIndex = n - 1
    leftWall = 0
    rightWall = 0
    waterUnit = 0

    while leftIndex <= rightIndex:
        if arr[leftIndex] < arr[rightIndex]:
            if leftWall < arr[leftIndex]:
                leftWall = arr[leftIndex]
            else:
                waterUnit += leftWall - arr[leftIndex]
            leftIndex += 1
        else:
            if rightWall < arr[rightIndex]:
                rightWall = arr[rightIndex]
            else:
                waterUnit += rightWall - arr[rightIndex]
            rightIndex -= 1
    return waterUnit


if __name__ == "__main__":
    print(trappingWater([3, 0, 0, 2, 0, 4], 6))
