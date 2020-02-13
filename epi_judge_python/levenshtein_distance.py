from test_framework import generic_test

# 16.2 Compute the Levenshtein distance
def levenshtein_distance(A, B):
    def calc_distance_between_prefixes(A_idx, B_idx):
        if A_idx < 0:
            return B_idx + 1
        if B_idx < 0:
            return A_idx + 1
        if distance_between_prefixes[A_idx][B_idx] == -1:
            if A[A_idx] == B[B_idx]:
                distance_between_prefixes[A_idx][B_idx] = (
                    calc_distance_between_prefixes(A_idx-1, B_idx-1))
            else:
                substitute_last = calc_distance_between_prefixes(A_idx-1, B_idx-1)
                add_last = calc_distance_between_prefixes(A_idx-1, B_idx)
                remove_last = calc_distance_between_prefixes(A_idx, B_idx-1)
                distance_between_prefixes[A_idx][B_idx] = 1 + min(
                    substitute_last, add_last, remove_last)
        return distance_between_prefixes[A_idx][B_idx]

    distance_between_prefixes = [[-1] * len(B) for _ in A]
    return calc_distance_between_prefixes(len(A) - 1, len(B) - 1)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
