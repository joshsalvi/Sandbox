# flips a bit in the binary number "number" at the nth place from the right
def flip_bit(number,n):
    mask = (0b1 << n-1)
    return bin(number ^ mask)
    