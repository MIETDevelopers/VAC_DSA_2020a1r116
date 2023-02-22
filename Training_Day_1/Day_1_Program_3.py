#python proogram to check is the no is even or odd using bit manipulation
num = int(input("Enter a number"))
if (num & 1) == 0:
    print("Number is even")
else :
    print("number is odd")