#program to check if the given number is armstrong or not
num = int(input())
digit = len(str(num))
sum_of_digit = 0
temp = num
while temp:
    rem = temp % 10
    sum_of_digit += rem**digit
    temp //= 10

if sum_of_digit == num:
    print(num, "is an armstrong number")
else:
    print(num, "is not an armstrong number")