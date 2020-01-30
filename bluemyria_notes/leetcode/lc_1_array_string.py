# 2D Array -  Diagonal Traverse
# input [[1,2,3],[4,5,6],[7,8,9]]
def findDiagonalOrder(matrix):
    rmax = len(matrix)
    if rmax == 0:
        return []
    cmax = len(matrix[0])
    res = []
    print(rmax, cmax)
    ri = ci = 0
    direction = 'up'
    while 0 <= ri < rmax and 0 <= ci < cmax:
        res.append(matrix[ri][ci])
        print(ri,ci,matrix[ri][ci])
        if direction == 'up':
            ci += 1
            ri -= 1
            print(ri,ci,"up")
            if ri < 0 and ci < cmax:
                ri = 0
                direction = 'down'
                print(ri,ci, direction, "next: correct 1")
            if ci == cmax:
                ci = cmax-1
                ri += 2
                direction = 'down' 
                print(ri,ci, direction, "next: correct 2")   
        elif direction == 'down':
            ci -= 1
            ri += 1
            print(ri,ci,"down")
            if ci < 0 and ri < rmax:
                ci = 0
                direction = 'up'
                print(ri,ci, direction,"next: correct 3")    
            if ri == rmax:
                ri = rmax-1
                ci += 2
                direction = 'up'
                print(ri,ci, direction,"next: correct 4")
        print(ri,ci, direction)
        print(res)
    return res

print(findDiagonalOrder([['a','b','c',1],['d','e','f',2],['g','h','i',3]]))
print(findDiagonalOrder([[],[],[]]))
print(findDiagonalOrder([]))


# Spiral Matrix
# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
def spiralOrder(matrix):
    def order_top(start, end, row):
        idx = start
        while idx <= end:
            res.append(matrix[row][idx])
            idx += 1
            
    def order_right(start, end, column):
        idx = start
        while idx <= end:
            res.append(matrix[idx][column])
            idx += 1
            
    def order_bottom(start, end, row):
        idx = start
        while idx >= end:
            res.append(matrix[row][idx])
            idx -= 1
            
    def order_left(start, end, column):
        idx = start
        while idx >= end:
            res.append(matrix[idx][column])
            idx -= 1
    
    ymax = len(matrix)
    if ymax == 0:
        return []
    xmax = len(matrix[0])
    res = []
    
    l = t = 0
    r = xmax - 1
    b = ymax -1
    
    while l < r and t < b:
        print(t,b,l,r)
        order_top(l, r-1, t )
        print(res)
        order_right(t, b-1, r )
        print(res)
        order_bottom(r, l+1, b )
        print(res)
        order_left(b, t+1, l )
        print(res)
        l += 1
        r -= 1
        t += 1
        b -= 1
        print("candidate",t,b,l,r)
    if xmax <= ymax and xmax%2 == 1:
        order_right(t,b,r)
    elif ymax < xmax and ymax%2 == 1:
        order_top(l,r,t)
    return res

print(spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]))            
print(spiralOrder([
 [1, 2, 3, 4],
 [5, 6, 7, 8],
 [9,10,11,12]
])) 

print(spiralOrder([
 [1, 2, 3],
 [4, 5, 6],
 [7, 8, 9],
 [10, 11, 12]
])) 

# Pascal's Triangle
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
def generate(numRows):
    
    def gen_step(level):
        if level == 0:
            return [1]
        if level == 1:
            return [1,1]
        part_res = [1] + [ res[level-1][i-1] + res[level-1][i] for i in range(1, level) ] + [1]
        return part_res

    res = [[]]* numRows
    print(res)
    
    for i in range(numRows):
        res[i] = gen_step(i)
    return res
    

print(generate(7))

#Add Binary
#Given two binary strings, return their sum (also a binary string).
#The input strings are both non-empty and contains only characters 1 or 0.
def addBinary(a,b):
    lenA = len(a)
    lenB = len(b)
    
    minstr = a if lenA <= lenB else b
    maxstr = a if lenA > lenB else b
      
    minlen = len(minstr)
    maxlen =  len(maxstr)
    print(minlen,maxlen)
    res =  [0] * (maxlen + 1)
    print(res)
    
    i = 0
    carry = 0
    while i < maxlen:
        print(i, minlen-1-i, maxlen-1-i)
        myres = int(maxstr[maxlen-1-i]) + carry
        myres += 0 if minlen-1-i < 0 else int(minstr[minlen-1-i])
        res[i] = myres % 2
        carry = myres // 2
        i += 1
    if carry == 1:
        res[i] = 1
    else:
        del res[i]
    print(res)
    res.reverse()
    return ''.join(str(i) for i in res)

print(addBinary('100101','110'))
print(('100101','110'))
    
print(addBinary('10010111','11'))
print(('10010111','11'))
    

#Implement strStr().
#Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
def strStr(haystack: str, needle: str) -> int:

    def findCharFromIdx(char: str, idx: int) -> int:
        ih = idx
        while ih < len(haystack) and haystack[ih] != char:
            ih += 1
        if ih == len(haystack):
            return -1
        else:
            return ih
    
    def findFromIdx(idx):
        for i in range(0, len(needle)):
            #print(haystack[idx + i], needle[i])
            if idx + i > len(haystack)-1 or haystack[idx + i] != needle[i]:
                return False
        return True
    
    if not needle:
        return 0
    if not haystack or len(haystack) < len(needle):
        return -1

    if len(needle)>30000:
        return haystack.index(needle) if needle in haystack else -1
    
    search_idx = findCharFromIdx(needle[0], 0)
    while search_idx != -1:
        if findFromIdx(search_idx):
            return search_idx
        else:
            search_idx = findCharFromIdx(needle[0], search_idx+1)
    return -1
    
print(strStr('sdfsdfsdfasdsdfasdf','asd'))

print(strStr('mississippi','issip'))

print(strStr(
"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
,"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
))

# Longest Common Prefix
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
def longestCommonPrefix(strs):
    if not strs:
        return ''
    idx = 0
    minlen = min([len(st) for st in strs])      
    while idx < minlen:
        if all(st[idx] == strs[0][idx] for st in strs):
            idx += 1
        else:
            break
    return strs[0][0:idx]

print('***-',longestCommonPrefix(['abcdef','abc','ab']),'-***')

print('***-',longestCommonPrefix(['abcdef','abc','de']),'-***')


# 344. Reverse String
# Easy
# Write a function that reverses a string. The input string is given as an array of characters char[].
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# You may assume all the characters consist of printable ascii characters.
def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    slen = len(s)
    k = slen//2
    if slen <= 1:
        return s
    for i in range(k):
        s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
    return s
print(reverseString(['H','a','l','l','o']))



# Array Partition I
# Easy
# Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.
def arrayPairSum(nums):
    nums.sort()
    return sum(nums[::2]) 
print(arrayPairSum([1,4,3,2]))

# 167. Two Sum II - Input array is sorted
# Easy
# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.
class Solution:
    # brute force
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            print(i)
            for j in range(i+1, len(nums)):
                print(j)
                if nums[i]+nums[j]==target:
                    return [i,j]
        return []

s = Solution()
print(s.twoSum([2,7,23,34],9))


def twoSum(numbers, target):
        l, r = 0, len(numbers)-1 
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [l+1, r+1]
            elif sum > target:
                r -= 1
            else:
                l += 1
print(twoSum([2,7,11,15],9))

# Remove Element
# Easy
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
def removeElements(nums, val):
    to_ins, curr, lennums = 0, 0, len(nums)
    while curr < lennums:
        if nums[curr] != val:
            nums[to_ins] = nums[curr]
            to_ins += 1
        curr += 1
    return to_ins

print(removeElements([0,1,2,2,3,0,4,2], 2))

# 485. Max Consecutive Ones
# Easy
# Given a binary array, find the maximum number of consecutive 1s in this array.
def findMaxConsecutiveOnes(nums):
    last_max, curr_max = 0, 0
    for i, val in enumerate(nums):
        if val == 1:
            curr_max += 1
        else:
            last_max = max(last_max, curr_max)
            curr_max = 0
    return max(last_max, curr_max)

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))


#Minimum Size Subarray Sum
#Given an array of n positive integers and a positive integer s, find the minimal
#length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
def minSubArrayLen(s, nums):
    if not nums:
        return 0
    left, nsum, l = 0, 0, len(nums)
    min_sub_len = 2 * l
    
    for right in range(l):
        nsum += nums[right]
        while nsum >= s:
            min_sub_len = min(min_sub_len, right-left+1)
            nsum -= nums[left]
            left += 1
    return 0 if min_sub_len == 2 * l else min_sub_len
    
def minSubArrayLen2(s, nums):
    # timeouts for large inputs
    if not nums:
        return 0
    min_sub_len = 2 * len(nums)
    sums = [0] * len(nums)
    sums[0] = nums[0]
    for i in range(1, len(nums)):
        sums[i] = sums[i-1] + nums[i]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (sums[j] - sums[i] + nums[i] >= s):
                min_sub_len = min(min_sub_len, j - i + 1)
                break
    return 0 if min_sub_len == 2 * len(nums) else min_sub_len

print(minSubArrayLen2(7, [2,3,1,2,4,3]))

# Rotate Array
# Given an array, rotate the array to the right by k steps, where k is non-negative.
def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    for i in range(k%l):
        nums[i], nums[(i+k)%l] = nums[(i+k)%l], nums[i]
    print(nums)


print(rotate([1,2,3,4,5,6,7], 3))


#Reverse Words in a String III
#Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
#Example 1:
#Input: "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
#Note: In the string, each word is separated by single space and there will not be any extra space in the string.

def reverseWords(s: str) -> str:
    return " ".join([w[::-1] for w in s.split()])

print(reverseWords("Let's take LeetCode contest"))


# Remove Duplicates from Sorted Array
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
def removeDuplicates(nums) -> int:
    ridx, widx, l = 0, 0, len(nums)
    while ridx < l:
        if nums[ridx] != nums[widx]:
            widx += 1
            nums[widx] = nums[ridx]
        ridx += 1
        print(nums)
    return widx + 1

print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))

# Pascal's Triangle II
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
# Note that the row index starts from 0.
def getRow(rowIndex: int):
    if rowIndex <= 1:
        return [1] * (rowIndex + 1)
    res = [1, 1]
    for j in range(2, rowIndex+1):
        for i in range(j-1):
            res[i] = res[i] + res[i+1]
        res[:1] = [1, res[0]]
    return res

print(getRow(0))
print(getRow(1))
print(getRow(3))
print(getRow(4))

# Move Zeroes
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Example: Input: [0,1,0,3,12] Output: [1,3,12,0,0]
def moveZeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    ridx, widx, l = 0, 0, len(nums)
    while ridx < l:
        if nums[ridx] != 0:
            nums[widx] = nums[ridx]
            widx += 1
        ridx += 1
    while widx < l:
        nums[widx] = 0
        widx += 1
    return nums

print(moveZeroes([0,1,0,3,5,0,0,0,12]))     