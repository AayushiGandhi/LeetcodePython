def lengthOfLongestSubstring(s):
    result = []
    count, maxi = 0, 0

    if len(s) <= 0 or len(s) >= 5 * (10 ** 4):
        return 0
    for i in s:
        if i == ' ':
            i = 99
        if i not in result:
            result.append(i)
            count = count + 1
        else:
            if count > maxi:
                maxi = count
            result = result[result.index(i)+1:]
            result.append(i)
            count = len(result)
    if count > maxi:
        maxi = count
    return maxi


if __name__ == "__main__":
    print(lengthOfLongestSubstring("this is a house"))
