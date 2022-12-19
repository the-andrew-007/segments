def sum_of_segments(segments: list[tuple[int, int]]) -> int:
    all_sum = 0
    # for seg in segments:
    #     all_sum += seg[1] - seg[0]
    not_intersected_segments = []
    for i, seg in enumerate(segments):
        # not_intersected_segments.append(seg)
        # all_sum += seg[1] - seg[0]
        append_new_segment_or_extend(not_intersected_segments, seg)

    print('all_sum', all_sum)


def append_new_segment_or_extend(not_intersected_segments: list[tuple[int, int]], segment: tuple[int, int]):
    for seg in not_intersected_segments:
        print(seg)


def if_intersec(seg1: tuple[int, int], seg2: tuple[int, int]) -> bool:
    if seg1[0] >= seg2[0] and seg1[0] <= seg2[1]:
        return True
    if seg1[1] >= seg2[0] and seg1[1] <= seg2[1]:
        return True
    return False


sum_of_segments([(2, 5), (4, 7), (4, 9)])
