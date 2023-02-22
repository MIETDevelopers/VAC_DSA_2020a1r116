#program to print all the perfect numbers from 1 to n

n = int(input())

for num in range(1, n+1):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    if sum(divisors) == num:
        print(num, "is a perfect number")