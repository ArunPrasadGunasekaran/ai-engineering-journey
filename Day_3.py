#Day3 Exercise
from unittest import skip

#Exercise_1
for number in range(1,11):
    print(number)

#Exercise_2
for number in range(1,20):
    if number % 2 == 0:
        print(number)

#Exercise_3
number=int(input("Enter a number: "))
x=1
while x <= number:
    print(x)
    x+=1

#Exercise_4
number=int(input("Enter a number: "))
for x in range(1,11):
    print(f'{number} * {x} = {x*number}')

#Exercise_5
x=0
for i in range(1,101):
        x=i+x
print(x)

#Exercise_6
for x in range(1,11):
    if x==6:
        break
    print(x)

#Exercise_7
for x in range(1,11):
    if x==5:
        continue
    print(x)

 #challenge_1
number=int(input('Enter a number: '))
print(f'number : {number}')
print(f'square:{number**2}')
print(f'cube: {number**3}')

# challenge_2
for x in range(1,6):
    number = int(input('Enter a number for square it: '))
    print(f'number : {number}')
    print(f'square:{number ** 2}')
    print(f'cube: {number ** 3}')









