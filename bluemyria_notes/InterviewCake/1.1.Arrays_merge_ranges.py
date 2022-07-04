import unittest

def merge_ranges(meetings):
    sorted_meetings = sorted(meetings)

    merged_meetings = [sorted_meetings[0]]

    for curr_meeting_start, curr_meeting_end in sorted_meetings[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]
        if curr_meeting_start <= last_merged_meeting_end:
            merged_meetings[-1] = (last_merged_meeting_start, 
                                   max(last_merged_meeting_end, curr_meeting_end))
        else:
            merged_meetings.append((curr_meeting_start, curr_meeting_end ))
    print(meetings)
    print(merged_meetings)
    return merged_meetings

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)], [(0, 1), (3, 8), (9, 12)]),
        ([(1, 2), (2, 3)], [(1,3)]),
        ([(1, 5), (2, 3)], [(1, 5)]),
        ([(1, 10), (2, 6), (3, 5), (7, 9)], [(1, 10)]),
        ([(1, 3), (2, 4)], [(1, 4)])
    ]

    def test_merge_ranges(self):
        for [test_array, expected] in self.data:
            actual = merge_ranges(test_array)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()    