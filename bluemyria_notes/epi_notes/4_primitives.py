import sys
import math

def count_bits(x):
    num_of_bits = 0
    while x:
        num_of_bits += x & 1
        # ToNote
        x = x >> 1
    print(num_of_bits)

count_bits(3)
count_bits(4)
count_bits(37)

# ToNote
print(sys.maxsize)
print(2**63 - 1)

# ToNote
print(sys.float_info)
print(bin(8))
print(bin(8>>1))
print(bin(8>>2))
print(bin(-16))
print(bin(-16>>2))
print(int("-0b100",2))
print(bin(1<<10))
print(bin(~0))
print(bin(15^5))
print(bin(~10))
print(bin(~1))
print(bin(~2))
print(bin(~3))
print(float("inf")-float("inf")/2)

print(abs(-34.5))
print(math.ceil(2.17))
print(math.floor(3.14))
print(math.ceil(3.5))
print(math.floor(3.5))
print(min(4, -4))
print(max(3.14, 3))
print(pow(2.71, 3.14))
print(2.71 ** 3.14)
print(math.sqrt(225))
