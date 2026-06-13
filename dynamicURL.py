from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def getuser(user_id: int): #to accept input only in integer
    return{"userid":user_id}

#if no name, it should return none
@app.get("/NAME")
def get_user_name(name: str = None): #if no name the it should show null (i.e None)
    return {"name": name}
#if you want to print a name, type /NAME?name=praditha in the url

@app.get("/items")
def get_items(name: str = None, price: int = 0): #default parameter
    return {
        "name": name,
        "price": price
    }
#if you want to print a name and price, type /items?name=cake&price=300 in the url

# Using POST method instead of using GET 
# To access POST method, you need to use swagger api to process requests
# use /docs to open swagger UI
@app.post("/USER")
def create_user(name: str, age: int, clg:str, sem: int):
    return{
        "message": "User created!",
        "data": {
            "name": name,
            "age": age,
            "College": clg,
            "Semester": sem
        }
        
    }

#create a class for just validation
from pydantic import BaseModel
class User(BaseModel): #Used inheritance
    name: str
    age: int

@app.post("/create_user")
def validation(user: User):
    return {
        "message": "User created!",
        "data": user
    }


class Address(BaseModel):
    city: str
    pincode: int

class User(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/create_user_again")
def create_user(user: User):
    return user