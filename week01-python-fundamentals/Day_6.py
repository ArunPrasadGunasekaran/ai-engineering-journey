#Day 6 Exercises

#Exercise_1 String Basics

print("Exercise_1")
text = "Python is powerful"
print(text[0])
print(text[-1])
print(text[:7])
print(text[::-1])
print(text.upper())
print(text.lower())

#Exercise 2 — String Processing

print("Exercise_2")
text_2 = "  Arun is learning Python and AI  "
print(text_2.strip())
print(text_2.upper())
print("Python" in text_2)
text_2=text_2.replace("Arun","Prasad")
print("Python" in text_2)
words=text_2.split()
print(words)

#Exercise 3 — Skills

print("Exercise_3")
skills = ["Python", "SQL", "Azure", "AI"]

join_skills= ", ".join(skills)
print(join_skills)

split_skills=join_skills.split(", ")
print(split_skills)

#Exercise 4 — List Comprehension
print("Exercise_4")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_numbers=[number**2 for number in numbers ]
print(square_numbers)

#Exercise 5 — Even Numbers

print("Exercise_5")
numbers = [1,2,3,4,5,6,7,8,9,10]
even_number=[number for number in numbers if number%2==0]
print(even_number)

#Exercise 6 — Input Validation

print("Exercise_6")
try:
    user_age=int(input("Enter Your Age: "))
except ValueError:
     print("User entering text instead of a number.")

#Exercise 7 — Calculator With Error Handling

print("Exercise_7")
try:
    first_number = int(input("Enter first number:"))
    second_number = int(input("Enter second number:"))
    divide_number = first_number/second_number
    print(f'divided_number: {divide_number}')
except ValueError:
    print("User entering text instead of a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

#Exercise 8 — AI-Oriented Exercise

print("Exercise_8")
user_text= "   I want to learn Python and AI   "
#Remove extra spaces.
extra_space=user_text.strip()
print(extra_space)

#Convert it to lowercase.
lowercase=extra_space.lower()
print(lowercase)

#Check whether "python" exists.
print("python" in lowercase)

#Split it into words.
word=((lowercase).split())
print(word)

#Print the number of words.
print(''.join(lowercase))

#count
print(len(word))









