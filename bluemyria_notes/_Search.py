def bubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        for j in range (i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
        print(alist)

def shortBubbleSort(alist):
    for i in range(len(alist)-1,0,-1):
        exchange = False
        for j in range (i):
            if alist[j] > alist[j+1]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                exchange = True
        if not exchange:
            print("raus")
            return    
        print(alist)


def selectionSort(alist):
    for i in range(len(alist)-1, -1, -1):
        max_idx = i
        max_value = alist[i]
        for j in range(i):
            if alist[j] > max_value:
                max_idx = j
                max_value = alist[j]     
        alist[max_idx], alist[i] = alist[i], alist[max_idx]
        print(alist)


def insertionSort(arr):
    for i in range(len(arr)):
        curr_val = arr[i]
        k = i
        while k >= 1 and arr[k-1] > curr_val:
            arr[k] = arr[k-1]
            k -= 1
        arr[k] = curr_val
        print(arr)


def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        # from here insertion sort w/ gap instead of 1 (see line 34++)
        for i in range(gap, n):
            curr_val = arr[i]
            k = i
            while k >= gap and arr[k-gap] > curr_val:
                arr[k] = arr[k-gap]
                k -= gap
            arr[k] = curr_val 
        gap //= 2


def mergeSort(arr):
    print("Splitting ", arr)
    if len(arr) > 1:
        mid = len(arr)//2
        lefthalf = arr[:mid]
        righthalf = arr[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)

        print("Merging ", lefthalf, righthalf)
        l, r, k = 0, 0, 0
        while l < len(lefthalf) and r < len(righthalf):
            if lefthalf[l] < righthalf[r]:
                arr[k] = lefthalf[l]
                l += 1
            else:
                arr[k] = righthalf[r]
                r += 1
            k += 1
        while l < len(lefthalf):
            arr[k] = lefthalf[l]
            k += 1
            l += 1
        while r < len(righthalf):
            arr[k] = righthalf[r]
            r += 1
            k += 1



def quickSort(alist):
    
    def quickSortHelper(arr, l, r):
        if l < r:
            print("quickSortHelper", l, r)
            idx = partition(arr, l, r)
            quickSortHelper(arr, l, idx-1)
            quickSortHelper(arr, idx+1, r)

    def partition(arr, l, r):
        val = arr[r]
        start, end = l, r-1
        done = False
        print("partition", l, r)
        while not done:
            while start <= end and arr[start] < val:
                start += 1
                print("start", start)
            while start <= end and arr[end] > val:
                end -= 1
                print("end", end)
            if end < start:
                done = True
                print("done")
            else:     
                arr[start], arr[end] = arr[end], arr[start] 
        arr[r], arr[start] = arr[start], arr[r]
        print("partition_end:", start, arr)
        return start

    quickSortHelper(alist, 0, len(alist)-1)



print("-----bubble sort----------")
alist = [54,26,93,17,77,31,44,55,20]
bubbleSort(alist)
print(alist)
print("-----short bubble sort----------")
alist = [54,26,93,17,77,31,44,55,20]
shortBubbleSort(alist)
print(alist)
print("-----selection sort----------")
alist = [54,26,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)
print("-----insertion sort----------")
alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)
print("-----shell sort----------")
alist = [54,26,93,17,77,31,44,55,20]
print("start: ", alist)
shellSort(alist)
print(alist)
print("-----merge sort----------")
alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
print("-----quick sort----------")
alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)