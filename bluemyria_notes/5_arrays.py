A = [0, 1, 2, 3, 4, 5, 6]
print(A[2:4]) 
print(A[2:]) 
print(A[:4]) 
print(A[:-1])
print(A[-3:])
print(A[-3:-1]) 
print(A[1:5:2]) 
print(A[5:1:-2])
print(A[::-1]) 
k=3
print(A[k:] + A[:k]) 
B = A[:]
print(B)

A = [1, 6, 3, 4, 5, 2, 77]
print(A[2:4]) # [3, 4]
print(A[2:]) #[3, 4, 5, 2, 77]
print(A[:4]) #[1, 6, 3, 4)
print(A[:-1]) #[1, 6, 3, 4, 5, 2]
print(A[-3:]) #[5, 2,77,
print(A[-3:-1]) # [5,2]
print(A[1:5:2]) #[6, 4]
print(A[5:1:-2]) #[2, 4]
print(A[::-1]) # [7, 2, 5, 4, 3, 6, 1] (reverseslist). 
#Slicing can also be used to rotate a list 
k=3
print(A[k:] + A[:k]) # rotates A by k to the left
# Itcanalsobeusedtocreateacopy: 
B = A[:]
print(B) # doesa(shallow)copyof Ainto B.