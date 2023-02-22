#program to check if the given digits of a number are even or odd in 2-digit number
number = int(input("Enter a number: "))
even_count = 0
odd_count = 0

while number > 0:
    digit = number % 10
    if digit % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    number //= 10

print("Number of even digits:", even_count)
print("Number of odd digits:", odd_count)