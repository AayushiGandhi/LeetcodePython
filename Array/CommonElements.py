import sys

#not working for negative elements

def commonElements(A, B, C, n1, n2, n3):
    p1 = 0
    p2 = 0
    p3 = 0
    prev1 = prev2 = prev3 = -sys.maxsize - 1
    result = []

    while p1 < n1 and p2 < n2 and p3 < n3:
        while p1 < n1 and A[p1] == prev1:
            p1 += 1
        while p2 < n2 and B[p2] == prev2:
            p2 += 1
        while p3 < n3 and C[p3] == prev3:
            p3 += 1

        if (p1 < n1 and p2 < n2 and p3 < n3) and (A[p1] == B[p2] == C[p3]):
            result.append(A[p1])
            prev1 = A[p1]
            prev2 = B[p2]
            prev3 = C[p3]
            p1 += 1
            p2 += 1
            p3 += 1


        elif p1 < n1 and A[p1] < B[p2]:
            prev1 = A[p1]
            p1 += 1

        elif p2 < n2 and B[p2] < C[p3]:
            prev2 = B[p2]
            p2 += 1

        elif p3 < n3:
            prev3 = C[p3]
            p3 += 1

    return result


if __name__ == "__main__":
    print(commonElements([-99, -96, -92, -91, -90], [-90, -89, -88, -99, -88], [-99, -81, -79, -76, -72 ], 5, 5, 5))
