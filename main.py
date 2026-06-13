from fastapi import FastAPI #fastapi is module and FastAPI is the class

app = FastAPI() #create object and using this we will be calling all the functions and use fastapi
@app.get("/") #default home page
def home():
    return {"message":"Welcome FastAPI"}

@app.get("/aboutUs")
def home():
    return{"message": "This is about us page."}

@app.get("/Contact")
def home():
    return{"message": "Contact us on Linkedin."}

@app.get("/Login")
def home():
    return{"message": "Login"}