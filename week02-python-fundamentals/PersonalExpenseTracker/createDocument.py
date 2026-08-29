import json
s_no = 0
def add_to_doc(a,b,c,d):
    try:
        with open("MonthlyExpense.json", 'r') as file:
            load_file = json.load(file)
            s_no = max(int(key) for key in load_file.keys()) + 1
            print(load_file)
            expenses_doc = {}
            expenses_doc[s_no]= {
            "expense": b,
            "category": c,
            "dateandtime": d
                }
            load_file.update(expenses_doc)
            with open("MonthlyExpense.json", 'w') as file:
                json.dump(load_file, file, indent=4)
            print("Data saved successfully")

    except FileNotFoundError:
        expenses_doc = {}
        expenses_doc[1] = {
            "expense": b,
            "category": c ,
            "dateandtime": d
        }
        with open("MonthlyExpense.json", 'w') as file:
            json.dump(expenses_doc, file, indent=4)
            print("Data saved successfully")




