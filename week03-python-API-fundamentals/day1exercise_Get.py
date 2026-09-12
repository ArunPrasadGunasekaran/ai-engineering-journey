from fastapi import FastAPI

app = FastAPI()

#@app.get("/send_hello/{user_id}")
#def send_hello(user_id:int):
#    return(f"Hello world:{user_id}")


@app.get("/send_hello")
def send_hello(category:str):
    return(f"Hello world:{category}")


#Endpoint-1
@app.get("/helo")
def helo():
    return "hello arun"

#Endpoint-2
@app.get("/employee/{employeeID}")
def employee(employeeID:int):
    employeedetails={
     "employeeID": employeeID,
     "Message": "Good Evening"
    }
    return employeedetails

#Endpoint-3
@app.get("/employeeDepartment")
def employee_dep(dep:str):
    employeedetails={
     "EmployeeDEP": dep ,
     "Messsage" : "Good Evening"
    }
    return employeedetails