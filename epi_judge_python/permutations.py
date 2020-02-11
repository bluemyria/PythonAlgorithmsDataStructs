from test_framework import generic_test, test_utils

# 15.3 Generate permutations of an array
def permutations(A):
    # SOS!!! After calculating the permutations, switch values back!!
    def perm_helper(i):
        if i == len(A) - 1:
            result.append(A)
            return
        for j in range(i, len(A)):
            A[j], A[i] = A[i], A[j]
            perm_helper(i+1)
            A[j], A[i] = A[i], A[j]
            
    result = []
    perm_helper(0)
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
