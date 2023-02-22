# #program to take three number as an input and print the largest and the smallest number
num1, num2, num3 = map(int,input().split())
if (num1>num2) and (num1>num3):
    largest = num1
elif (num2>num1) and (num2>num3):
    largest = num2
else:
    largest = num3


if (num1<num2) and (num1<num3):
    smallest = num1
elif (num2<num1) and (num2<num3):
    smallest = num2
else:
    smallest = num3

print("The largest number is : ", largest)
print("The smallest number is : ", smallest)

