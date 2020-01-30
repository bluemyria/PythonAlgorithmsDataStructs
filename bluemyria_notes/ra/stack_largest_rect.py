#!/bin/python3

# Complete the largestRectangle function below.
def largestRectangle(h):
    st = []
    nr = len(h)
    rect = rect_max = 0
    for i, bld in enumerate(h):
        k = i
        while k < nr and h[k] >= bld:
            st.append(h[k])
            k += 1
        k = i-1
        while k >= 0 and h[k] >= bld:
            st.append(h[k])
            k -= 1
            
        if len(st) > 0:
            rect = bld * len(st)
        rect_max = max(rect, rect_max)
        rect = 0
        st = []
    return rect_max 


if __name__ == '__main__':
    
    st1 = [1, 3, 5, 9, 11]  # 18
    st2 = [11, 11, 10, 10, 10] # 50
    
    print(largestRectangle(st1))
    print(largestRectangle(st2))
