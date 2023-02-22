#write a program to toggle kth bit of the binary number
num = int(input("Enter a binary number: "))
k = int(input("Enter the bit to be toggled (0-indexed): "))
mask = 1<<(k-1)
num = num^mask
print("After toggling the bit, the binary number is:",num)