#Exercise 1

def greet():
    print('Hello, welcome to Python!')

greet()

#Exercise 2
def greet(name):
    print(f'Hello, {name}')

greet('Arun')

#Exercise 3

def addition(A , B):
    return A + B

print(addition(15,10))

#Exercise 4

def calculate(a):
    square = a ** 2
    cube = a ** 3
    return square , cube

square , cube = calculate(5)
print(f'square : {square}')
print(f'cube : {cube}')

#Exercise 5

def salary_calculator(salary):
    yearly_calculation = salary * 12
    return yearly_calculation/100000

print(salary_calculator(89000))
print(salary_calculator(90000))
print(salary_calculator(91000))

#Exercise 6
def check_score(score):
    if score >= 90:
        return 'A'
    elif score>= 75:
        return 'B'
    elif score>=50:
        return 'C'
    else:
        return 'D'

user_score=int(input('Enter your score: '))
print(f'Your_Grade : {check_score(user_score)}')

#Exercise 7
numbers = [10, 20, 30, 40, 50]

def calculate_square(number):
    return number ** 2

for number in numbers:
    print(calculate_square(number))

#Exercise 8 — AI-Oriented
def check_confidence(confidence):
    if confidence >= 0.80:
        return "High Confidence"
    elif confidence >= 0.50 :
        return "Medium Confidence"
    else:
        return "Low Confidence"

print(f'confidence : {check_confidence(0.87)}')



