#program to print the fibnacci series upto "N"
# input = 5
# output = 
# 0
# 1
# 1
# 2
# 3

nterms = int(input())
n1, n2 = 0, 1
count = 0
if nterms<=0:
    print("invalid")
elif nterms==1:
    print("Fibonacci series upto", nterms, ":")
    print(n1)
else:
    print("Fibonacci series : ")
    while count<nterms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
