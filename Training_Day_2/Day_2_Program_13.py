#program to calculate the sum of three number. If the values are equal, return three times their sum.

a,b,c = list(map(int,input().split()))
sum_of_no = a+b+c
print(sum_of_no)
if a==b==c:
    print(3*sum_of_no)
else:
    print(sum_of_no)