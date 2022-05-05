import math


def nextGap(gap):
    if gap <= 1:
        return 0
    return math.ceil(gap / 2)


def merge(arr1, arr2, n, m):
    gap = n + m
    gap = nextGap(gap)

    while gap > 0:
        pointer1 = 0

        while pointer1 + gap < n:
            if arr1[pointer1] > arr1[pointer1 + gap]:
                arr1[pointer1], arr1[pointer1 + gap] = arr1[pointer1 + gap], arr1[pointer1]
            pointer1 += 1

        pointer2 = gap - n if gap > n else 0
        while pointer1 < n and pointer2 < m:
            if arr1[pointer1] > arr2[pointer2]:
                arr1[pointer1], arr2[pointer2] = arr2[pointer2], arr1[pointer1]
            pointer1 += 1
            pointer2 += 1

        if pointer2 < m:
            pointer2 = 0
            while pointer2 + gap < m:
                if arr2[pointer2] > arr2[pointer2 + gap]:
                    arr2[pointer2], arr2[pointer2 + gap] = arr2[pointer2 + gap], arr2[pointer2]
                pointer2 += 1

        gap = nextGap(gap)
    print(arr1)
    print(arr2)


if __name__ == "__main__":
    merge([3, 27, 38, 43], [9, 10, 82], 4, 3)
