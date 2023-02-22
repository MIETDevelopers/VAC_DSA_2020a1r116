# program to calculate the electricity bill (accept number of unit from user) accordng to the following criteria:
# unit                            price
# first 100 unit                  no charge
# next 100 unit                   6 rs per unit
# after 200 unit                  8 rs per unit
# fix charge of rs 40 is applicable to all.
# i/p: 95 o/p: 40 rs only
# i/p: 165 o/p: 430 rs only
# i/p: 225 o/p: 840 rs only

unit = int(input())
if unit<=100:
    print("Your bill is Rs 40 only")
elif unit>100 and unit<=200:
    print("Your bill is Rs",(unit-100)*6+40,"only")
else:
    print("Your bill is Rs",(unit-200)*8+(100*6)+40,"only")
