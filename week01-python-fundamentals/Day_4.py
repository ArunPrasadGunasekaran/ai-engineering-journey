#Exercise_1 — List Basics

skills = ["Python", "SQL", "Mendix", "Azure"]
print(skills[0])
print(skills[-1])
skills.append("AI")
skills.pop(2)
print(skills)
print(len(skills))

#Exercise_2 — List + Loop

numbers = [10, 20, 30, 40, 50]
print(numbers)
for number in numbers:
    print(number**2)

#Exercise_3 — Remove Duplicates

skills = ["Python", "SQL", "Python", "Azure", "SQL", "AI"]
print(set(skills))

#Exercise_4 — Dictionary

employee = {
    "name": "Arun",
    "role": "Mendix Developer",
    "experience": 4,
    "city": "Neyveli"
    }
print(employee["name"])
print(employee["role"])
employee["role"]="AI Engineer"
employee["skills"]=["Python", "SQL", "Mendix"]
print(employee)

for x in employee.items():
    print(x)

#Exercise_5
user = {
    "name": "Arun",
    "age": 30,
    "skills": ["Mendix", "SQL", "Python"],
    "is_working": True
}
print('Exercise_5')
print(f"Skills: {', '.join(user['skills'])}")

#Exercise_6
user = {
    "name": "Arun",
    "age": 30,
    "skills": ["Mendix", "SQL", "Python"],
    "is_working": True
}
print("Exercise_6")
for x in user:
    if x=='skills':
        print(f'Primary skill: {user["skills"][0]}')
        print(f'Secondary skill: {user["skills"][1]}')
    elif x=='is_working':
        print(f'Currently Working : {user[x]}')
    else:
        print(f'{x} : {user[x]}')