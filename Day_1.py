#Day1 Exercise
from datetime import datetime

current_year = datetime.now().year


#first_name=input('Enter your first name: ')
#last_name=input('Enter your last name: ')
#city=input('your living in ? : ')
#birth_year=int(input('Enter your birth year: '))

Salary=float(input('Enter your Salary: '))

#print(f'Your Name is {first_name} {last_name}')
#print(f'living in {city}')
#print(f'You are {current_year-birth_year} year\'s old')
#print(f'Your fixed LPA is {(Salary*12/100000):.2f}')


print(f'Your monthly salary is : {Salary}')
print(f'Your Annual Salary is : {Salary*12}')
print(f'Your Fixed LPA is : {(Salary*12/100000):.2f}')



