#program to print odd number sequence below "N"
# input = 50
# output = 
# 1
# 3
# 5
# 7
# 9
# ..
# 49

num = int(input())
for i in range(1, num):
    if (i%2 != 0):
        print(i)

