#program to check the number is pallindrome or not
num = int(input())
temp = num
total = 0
while num:
    rem = num%10
    num //= 10
    total = total*10+rem
if(temp == total):
    print("The number is palindrome")
else:
    print("Not a palindrome")