

from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
class employee(BaseModel):
    name:str
    department:str
    experience:int
    salary: float
    employeeID:int

@app.post("/employee")
def create_Employee(Employee : employee):
    return Employee

