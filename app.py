from fastapi import FastAPI
from mydata import get_data
from hashtest import get_fruits_info

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}

@app.get("/user")
async def user_info():
    # mydata.py 결과
    return get_data()

@app.get("/fruits")
async def fruits_info():
    # HashSetExample.py 결과
    return get_fruits_info()
