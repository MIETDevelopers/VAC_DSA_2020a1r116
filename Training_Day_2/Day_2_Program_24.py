#program to find the factrial of a number using function

def factorial(num):

    fact = 1
    if num < 0:
        print("Invalid")
    elif num == 0:
        print("The factorial of 0 is 1")
    else:
        for i in range(1, num+1):
            fact *= i
        print("Factorial of", num, "is", fact)

num = int(input())
factorial(num)