#Sum/Average Program
#Your first and last name: Christian Ramos
#Your student ID: s1287151

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:

numberList = []
tot = 0

for x in range (0,20):
    num = int(input("Enter a number: "))
    numberList.append(num)

for y in range (0,20):
    tot = tot + numberList[y]
print("the sum is ", tot)
print("the average is ", tot/20)
