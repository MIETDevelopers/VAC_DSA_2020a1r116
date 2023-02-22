#program to find the absolute difference between set and unset bits
def abs_diff(n):
    binary = bin(n)[2:]
    set_bits = 0
    unset_bits = 0
    for bit in binary:
        if bit == '0':
            unset_bits += 1
        else:
            set_bits += 1
    print(binary)
    return abs(unset_bits - set_bits)

n = int(input("Enter the bit : "))
diff = abs_diff(n)
print(diff)