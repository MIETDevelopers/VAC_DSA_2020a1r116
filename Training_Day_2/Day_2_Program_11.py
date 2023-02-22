#program to greet differnt message depending on what time of day it is morning, afternoon, evening, or night (time is given in 24 hours format)
time = int(input("Enter the current time (in 24-hours format, without the colon) : "))
if time>=0 and time<1200:
    print("Good Morning!")

elif time>=1200 and time<1600:
    print("Good Afternoon!")   

elif time>=1600 and time<2000:
    print("Good Evening!")

elif time>=2000 and time<0:
    print("Good night!")

else:
    print("Invalid format")
