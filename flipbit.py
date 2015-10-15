# flips a bit in the binary number "number" at the nth place from the right
def flip_bit(number,n):
    if n > 0:
        mask = (0b1 << n - 1)
        return bin(number ^ mask)
    else:
        print "\nERROR: Must choose bit number greater than zero.\n"
        return bin(0b00000)


print int(flip_bit(12341, 30), 2)
