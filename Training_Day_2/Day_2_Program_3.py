#program to take 5 subject marks as an input calculate the percentage and also allocate the grade to the student criteria is the marks in individual subject is >33 and overall percentage is 40% and grade is second if the percentage >40 and <60 grade is first if percentage percentage is >60 and <80 the grade is excellent if the percentage is >80

listt = list(map(int,input().split()))
a,b,c,d,e = listt
percentage = (a+b+c+d+e)/5
if a>33 and b>33 and c>33 and d>33 and e>33 and percentage >= 40:
    print("The student is pass")
    if percentage>=40 and percentage<60:
        print("The grade is second")
    elif percentage>=60 and percentage<80:
        print("The grade is first")
    else:
        print("The grade is excellent")
    print(percentage)
else :
    print("The student is fail")
    print(percentage)

