#program to print the digit of a given number
num = int(input())
while num != 0:
    rem = num%10
    num //= 10
    print(rem)