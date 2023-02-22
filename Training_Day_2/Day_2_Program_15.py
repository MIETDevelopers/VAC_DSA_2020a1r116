#a student grade is calculated as "A" if the score is 90 and above,"B" if the score is 75 to 89,"C" if the score is 60 to 74, and "D" if the score is less than 60.
#program to display a "Cogratulation" if the grade of a student is either A or B,"Work Hard" if the grade is "C", and "Try next time", if the grade is "D" for the given score.

score = int(input())
grade = ''
if score>=90:
    grade = 'A'
elif score>=75 and score<=89:
    grade = 'B'
elif score>=60 and score<=74:
    grade = 'C'
else:
    grade = 'D'
print(grade)
if grade == 'A' or grade == 'B':
    print("Congratulations")
elif grade == 'C':
    print("Work Hard")
else:
    print("Try Next Time")