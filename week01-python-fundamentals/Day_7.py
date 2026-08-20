import json
import calculator
skills=['Python','SQL','AI','Azure','Mendix']
with open("ACT_UpdateTimelineRisk.txt", "r") as file:
    content = file.read()
    print("Option1")
    for i in content:
        print(i)
    print("Option2")
    file.seek(0)
    for i in file:
        print(repr(i))

#Exercise1
print("\nExercise_1Write")

with open("skill.txt", "w") as file:
    for i in skills:
        file.write(f"\n{i}")

#Exercise_2
print("\nExercise_2read_Content")
with open("skill.txt", "r") as file:
    content =file.read()
    print(content)

    print("\nExercise_2read_lineByline")
    file.seek(0)
    for i in file:
        print(i)

#Exercise_3
with open("skill.txt","a") as file:
     file.write("\nMachine Learning")
with open("skill.txt" ,"r") as file:
    content =file.read()
    print(content)

#Exercise_4
print("Exercise_4")

print(f'Addition: {calculator.add(50,20)}')
print(f'Subtraction: {calculator.subtract(50,20)}')
print(f'Multiply: {calculator.multiply(50,20)}')
print(f'Divide: {calculator.division(50,20)}')

#Exercise 5 — JSON
print("Exercise_5")
user = {
    "name": "Arun",
    "role": "Mendix Developer",
    "experience": 4,
    "skills": ["Python", "SQL", "AI"],
    "is_working": True
}

jsonString=json.dumps(user)
print(jsonString)
jsonFile=json.loads(jsonString)
print( f'User_Name: {jsonFile["name"]}')
print( f'User_Role: {jsonFile["role"]}')
print( f'User_Skills: {jsonFile["skills"]}')

#Exercise 6 — JSON
print(" Exercise 6 ")
employee = {
    "name": "Arun",
    "role": "Mendix Developer",
    "experience": 4,
    "skills": ["Python", "SQL", "AI"],
    "location": "India"
}

with open("employee.json","w") as file:
    json.dump(employee,file)

with open("employee.json","r") as file:
   readFile= json.load(file)
   for key in readFile:
    print(f'{key} : {readFile[key]}')

#Exercise 7 — Final Python Foundation Challenge ⭐⭐⭐
print("Exercise_7")

employees=[]
# Print all employees.
try:
    employees_count=int(input("How many employees data you need to store: "))
    print(f"employees_count: {employees_count}")
    for i in range(employees_count):
        employee = {}
        name = (input("Please add employee name: "))
        age = int(input("Please add employee Age:  "))
        salary = int(input("Please add employee Salary:  "))
        role = (input("Please add employee role:  "))
        employee_skills = []
        for i in range(2):
            skill = (input("Please add atleast two skills: "))
            employee_skills.append(skill)
        employee["name"] = name
        employee["age"]=age
        employee["salary"]=salary
        employee["role"]=role
        employee["skills"]=employee_skills
        employees.append(employee)
except ValueError:
    print(" Invalid Input")

print(employees)

# Calculate each employee's annual salary.

total_salary=0
for i in employees:
    total_salary=((i["salary"]*12)/100000)
    print(f"annual salary of {i['name']} = {total_salary}")

# Find employees whose salary is greater than 80000.

employees_with_higher_salary=[]
for i in employees:
    if i["salary"]>80000:
        employees_with_higher_salary.append(i)
print(f'Employees_With_Higher_salary : {employees_with_higher_salary}')


# Save the employee data to employees.json.

with open("List_Of_employees.json",'w') as file:
    json.dump(employees,file)

# Read the JSON file back and print the data.

with open("List_Of_employees.json",'r') as file:
    readfile=json.load(file)
    serialnumber=0
    print(readfile)
    for i in (readfile):
        serialnumber+=1
        print(f'{serialnumber}) {i["name"]} : {i}')













