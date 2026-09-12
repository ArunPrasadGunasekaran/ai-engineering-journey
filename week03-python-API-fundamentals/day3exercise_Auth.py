from fastapi import FastAPI , Header , HTTPException ,Depends
from pydantic import BaseModel
from fastapi.security import HTTPBasic , HTTPBasicCredentials
import logging
(logging.basicConfig
 (level=logging.INFO ,
  filename="day3.log"))


security= HTTPBasic()
app=FastAPI()
MyXApiKey='My-XApi-Key'
UserName='ArunPrasad'
Password='12345678'
@app.get("/welcome")
def welcome(X_Api_Key:str=Header(),credentials=Depends(security)):
    if X_Api_Key!=MyXApiKey :
        logging.warning("X-Api-Key is wrong")
        raise HTTPException (
            status_code=401 ,
            detail="Wrong X-Api-Key "
        )
    if credentials.username!=UserName :
        logging.warning("UserName is wrong")
        raise HTTPException (
            status_code=401 ,
            detail="Wrong username"
        )
    if credentials.password!=Password :
        logging.warning("Password is wrong")
        raise HTTPException (
            status_code=401 ,
            detail="Wrong Password"
        )
    logging.warning("Authentication Successfull")
    return("Welcome to the world")
