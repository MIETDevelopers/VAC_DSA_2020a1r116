#program to to test whether m is a factor of n
m,n = list(map(int,input().split()))
if n%m==0:
    print(m, "is a factor of", n)
else:
    print(m, "is not a factor of", n)