#program to find the total no of unset bits in a given number
def count_bits(n):
    binary = bin(n)[2:]
    set_bits = 0
    unset_bits = 0
    for bit in binary:
        if bit == '0':
            unset_bits += 1
        else:
            set_bits += 1
    print(binary)
    return (unset_bits,set_bits)

n = int(input("Enter the bit : "))
count = count_bits(n)
print(count)