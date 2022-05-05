#https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1#
def minJumps(arr, n):
    # code here
    if n <= 1:
        return 0

    if arr[0] == 0:
        return -1

    maxReach = arr[0]
    steps = arr[0]
    jumps = 1

    for i in range(1, n):
        if i == n - 1:
            return jumps
        maxReach = max(maxReach, i + arr[i])
        steps -= 1

        if steps == 0:
            jumps += 1

            if i >= maxReach:
                return -1

            steps = maxReach - i
    return -1


if __name__ == "__main__":
    print(minJumps([2, 1, 0, 3], 4))
