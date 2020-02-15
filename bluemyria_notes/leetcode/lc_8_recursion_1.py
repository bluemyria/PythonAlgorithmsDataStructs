# Reverse String
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    slen = len(s)
    k = slen//2
    if slen <= 1:
        return
    for i in range(k):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]

# Pascal's Triangle II
def getRow(self, rowIndex: int) -> List[int]:
    if rowIndex <= 1:
        return [1] * (rowIndex + 1)
    res = [1, 1]
    for j in range(2, rowIndex+1):
        for i in range(j-1):
            res[i] = res[i] + res[i+1]
        res[:1] = [1, res[0]]
    return res