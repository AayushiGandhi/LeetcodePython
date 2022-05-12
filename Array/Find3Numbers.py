def find3Numbers(A, n, X):
    A.sort()
    for index in range(n):
        pairSum = X - A[index]
        left = index + 1
        right = n - 1

        while left < right:
            if A[left] + A[right] == pairSum:
                return True
            elif A[left] + A[right] < pairSum:
                left += 1
            elif A[left] + A[right] > pairSum:
                right -= 1

    return False


if __name__ == "__main__":
    print(find3Numbers([4, 45, 6, 10, 8], 5, 24))
