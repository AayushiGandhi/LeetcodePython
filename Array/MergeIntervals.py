def merge(intervals):
    intervals.sort(key=lambda i: i[0])
    output = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= output[-1][1]:
            output[-1][1] = max(end, output[-1][1])
        else:
            output.append([start, end])
    return output


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals1 = [[1, 4], [4, 5]]
    intervals2 = [[1, 4], [1, 4]]
    intervals3 = [[1, 4], [0, 4]]
    intervals4 = [[1, 4], [2, 3]]
    intervals5 = [[1, 4], [0, 2], [3, 5]]
    print(merge(intervals))
    print(merge(intervals1))
    print(merge(intervals2))
    print(merge(intervals3))
    print(merge(intervals4))
    print(merge(intervals5))

'''
def merge(intervals):
    result = []
    intervals = sorted(intervals)

    while intervals:
        i = intervals[0]
        flag = False
        intervals.remove(i)
        for j in intervals:
            if i[0] <= j[0] <= i[1]:
                intervals.remove(j)
                result.append([ min(i[0], j[0]),  max(i[1], j[1])])
                flag = True

        if not flag:
            result.append(i)
    return result

'''
