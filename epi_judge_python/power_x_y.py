from test_framework import generic_test
import time

# 4.7 Compute x**y
# Write a program that takes a double x and an integer y and retuns x**y.
# You can ignore overflow and underflow.
def power(x, y):
    # SOS!!! 
    # if you have a negative y (power, turn it to positive.. see line 16)
    # SOS!!!
    # y>>1 is NOT the same as y = y>>1!!!!!!!!
    # if current last bit of y (power) == 1, multiply result *x  !!!
    # if current last bit of y (power) == 2, multiply x = x*x!!! (power of 2)
    result = 1.0
    if y < 0:
        x , y = 1/x , -y 
    while y:
        if y & 1:
            result *= x
        y = y >> 1
        x = x * x
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))
