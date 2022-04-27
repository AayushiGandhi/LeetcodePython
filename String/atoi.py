#https://leetcode.com/problems/string-to-integer-atoi
def myAtoi(s: str) -> int:
    s = s.strip()
    pos, sign = 1, 1
    value = ""

    if not s:
        return 0

    if s[0] == "-":
        sign = -1
    elif s[0] == "+":
        sign = 1
    else:
        if s[0].isdigit():
            value = s[0]
        else:
            return 0

    while pos < len(s):
        if s[pos].isdigit():
            value = value + s[pos]
        else:
            break
        pos = pos + 1

    sign = sign * int(value) if value else 0

    if sign < -(2 ** 31):
        sign = -(2 ** 31)
    elif sign > (2 ** 31) - 1:
        sign = (2 ** 31) - 1
    return sign


if __name__ == "__main__":
    print(myAtoi("+-12"))
    print(myAtoi("-91283472332"))
    print(myAtoi("-486574"))
    print(myAtoi("words and 987"))

