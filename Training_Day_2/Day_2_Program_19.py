# program to print even number sequence below "N"
# input = 50
# output =
# 2
# 4
# 6
# 8
# ...
# 48

num = int(input())
for i in range(1, num):
    if (i%2 == 0):
        print(i)