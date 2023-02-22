current_wizard = input()
count = 1
fights = int(input())
for i in range(fights):
    duo = input().split() # duo will be list or not
    if duo[1] == current_wizard:
        current_wizard = duo[0]
        count += 1
    elif duo[0] == current_wizard:
        current_wizard = duo[1]
        count += 1
print(current_wizard, count, sep='\n')