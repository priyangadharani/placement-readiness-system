from fastapi import FastAPI
app=FastAPI()
@app.get("/") 
def home():
    return{"message":"Placement Readiness System is running!" }