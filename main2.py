def sum_of_segments(segments: list[tuple[int, int]]) -> int:
    final_sum = 0

    while True:
        segments = try_clear_from_intersection(segments)
        if not has_intersections(segments):
            break

    for seg in segments:
        final_sum += seg[1] - seg[0]

    return final_sum


def has_intersections(segments: list[tuple[int, int]]) -> bool:
    list_to_check_intersec = []
    for i, seg1 in enumerate(segments):
        list_to_check_intersec.append(seg1)
        for seg2 in list_to_check_intersec:
            if seg1 != seg2:
                if is_intersec(seg1, seg2):
                    return True
    return False


def try_clear_from_intersection(segments: list[tuple[int, int]]) -> list[tuple[int, int]]:
    not_intersected_segments = []
    for i, seg in enumerate(segments):
        append_new_segment_or_extend(not_intersected_segments, seg)
        # print(not_intersected_segments)
    return not_intersected_segments


def append_new_segment_or_extend(not_intersected_segments: list[tuple[int, int]], segment_to_test: tuple[int, int]):
    if len(not_intersected_segments) == 0:
        not_intersected_segments.append(segment_to_test)
        return
    extended = False
    for i, seg in enumerate(not_intersected_segments):
        if is_intersec(seg, segment_to_test):
            # print('extend', segment_to_test)
            not_intersected_segments[i] = extend(seg, segment_to_test)
            extended = True
            break
    if not extended:
        # print('append', segment_to_test)
        not_intersected_segments.append(segment_to_test)


def is_intersec(seg1: tuple[int, int], seg2: tuple[int, int]) -> bool:
    if seg1[0] >= seg2[0] and seg1[0] <= seg2[1]:
        return True
    if seg1[1] >= seg2[0] and seg1[1] <= seg2[1]:
        return True
    if seg1[0] <= seg2[0] and seg2[0] <= seg1[1]:
        return True
    return False


def extend(seg1: tuple[int, int], seg2: tuple[int, int]) -> tuple[int, int]:
    return (min(seg1[0], seg2[0]), max(seg1[1], seg2[1]))

# print(sum_of_segments([(1, 17), (2, 15), (4, 14), (3, 16)]))
print(sum_of_segments([(1, 2), (6, 10), (11, 15)]))
# result is 9

print(sum_of_segments([(1, 4), (7, 10), (3, 5)]))
# result is 7

print(sum_of_segments([(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)]))
#result is 19 HERE

print(sum_of_segments([(0, 25), (-999999999, 15), (52, 62)]))
# result is 100000034

# print(has_intersections([(1, 5), (10, 20), (1, 6), (16, 19), (5, 11)]))
# print(has_intersections([(1, 4), (7, 10)]))
