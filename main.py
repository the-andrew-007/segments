def sum_of_segments(segments: list[tuple[int, int]]) -> int:
    result_sum = 0
    skip_index1 = -1
    skip_index2 = -1
    stop = False
    sum_intersec = 0
    for i, seg1 in enumerate(segments):
        for j, seg2 in enumerate(segments):
            if i == j:
                continue
            if if_intersec(seg1, seg2):
                sum_intersec += max(seg1[1], seg2[1]) - min(seg1[0], seg2[0])
    print('sum_intersec', sum_intersec)

    for i in range(len(segments) - 1):
        result_sum += (segments[i][1] - segments[i][0]) + (segments[i + 1][1] - segments[i + 1][0])
    print('result_sum', result_sum)

    return result_sum - sum_intersec


def if_intersec(seg1: tuple[int, int], seg2: tuple[int, int]) -> bool:
    if seg1[0] >= seg2[0] and seg1[0] <= seg2[1]:
        return True
    if seg1[1] >= seg2[0] and seg1[1] <= seg2[1]:
        return True
    return False


print(sum_of_segments([(2, 5), (8, 11), (4, 6)]))
