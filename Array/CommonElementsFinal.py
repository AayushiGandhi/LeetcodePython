#Using binary search tree
def binarySearchTree(arr, size, element):
    low, high = 0, size-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == element:
            return True
        elif element < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


def commonElements(A, B, C, n1, n2, n3):
    result = []
    for i in range(n1):
        if i != 0 and A[i] == A[i-1]:
            continue

        if binarySearchTree(B, n2, A[i]) and binarySearchTree(C, n3, A[i]):
            result.append(A[i])
    return result


if __name__ == "__main__":
    print(commonElements([1, 5, 20, 20, 40, 80], [6, 7, 20, 80, 100], [3, 4, 15, 20, 30, 70, 80, 120 ], 6, 5, 8))
