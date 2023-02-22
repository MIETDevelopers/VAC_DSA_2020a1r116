#program to print below to given age:-->
# i) age<18 "Sorry tou are still minor"
# ii) age between 18 and 21 "Congrats you are major but not eligible for marriage"
# iii) age>21 "Congrats you are major and eligible for marriage"

age = int(input())
if age<18:
    print("Sorry tou are still minor")
elif age>=18 and age<21:
    print("Congrats you are major but not eligible for marriage")
else:
    print("Congrats you are major and eligible for marriage")
