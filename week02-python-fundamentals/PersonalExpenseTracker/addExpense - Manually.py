from enum import Enum

from sympy import true

import createDocument as CD
from datetime import datetime
import json



class ExpenseCategory(Enum):
    FOOD = "Food"
    SHOPPING = "Shopping"
    GROCERY = "Grocery"
    PETROL = "Petrol"
    MISCELLANEOUS = "Miscellaneous"


print("List of Category:")
run_program=True
while run_program:
    for category in ExpenseCategory:
        print(category.value)
    Input_category = input('\nSelect Expense Category:',)
    categories=[category.value for category in ExpenseCategory]
    if Input_category not in categories:
        print("Selected Category is not available")
        exit()
    else:
        amount=int(input('Amount:'))
        DateNow=datetime.now().isoformat()
        #sl_No=int(input('Sl.No:'))
        sl_no=''
        CD.add_to_doc(sl_no,amount,Input_category,DateNow)
        WantToAdd=input("want to add more , yes or no ? : ")
        if WantToAdd!='yes':
            run_program=False
















