#program to give the grades to students and the criteria is if the marks is less than 40 the student is fail the marks between 40-50 the grade is C if the marks is in 50-60 th grade is B if the marks is greater than 60 the grade is A
marks = float(input())
if marks<=40:
    print("The Student is Fail...!!!")
elif marks>40 and marks<=50:
    print("The Grade is C")
elif marks>50 and marks<=60:
    print("The Grade is B")
else:
    print("The Grade is A")