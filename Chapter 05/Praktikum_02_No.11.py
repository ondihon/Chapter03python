from random import choice
 
# list of numbers
numList = [10, 23, 22, 34, 12]
 
# memilih bil dari list scr acak
for i in range(5):
    bil = choice(numList)
    print(bil)
