import json
def total_spent():
    with open("MonthlyExpense.json", 'r') as file:
        load_file = json.load(file)
        total=0
        for amount in load_file:
            total+=int(load_file[amount]["expense"])
        print(f"our total expenses: {total}")


def total_spent_category(a):
    with open("MonthlyExpense.json", 'r') as file:
        load_file = json.load(file)
        total=0
        for amount in load_file:
            if load_file[amount]["category"]==a:
                total+=int(load_file[amount]["expense"])
        print(f"Your total spent on {a} =  {total}")

total_spent()

expense_by_category=input("Enter category: ")
total_spent_category(expense_by_category)