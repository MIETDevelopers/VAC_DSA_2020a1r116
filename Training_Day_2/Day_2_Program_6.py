#program to find the absolute difference between the addition of even and odd digits 

num = int(input())
odd_sum = 0
even_sum = 0
while num:
    digit = num %10
    if digit % 2 == 0:
        even_sum += digit
    else:
        odd_sum += digit
    num //= 10

abs_diff = abs(even_sum - odd_sum)
print(abs_diff)
