from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

USER_DB = {}

NAME_NOT_FOUND = HTTPException(status_code=400, detail="Name not found")

class CreateIn(BaseModel): #입력받아야 하는 데이터
    name: str
    nickname: str

class CreateOut(BaseModel): #반환하고자 하는 데이터
    status: str
    id: int

@app.post("/users", reponse_model=CreateOut)
def create_user(user: CreateIn) -> CreateOut:
    USER_DB[user.name] = user.nickname
    return CreateOut(status="success", id=len(USER_DB))

@app.get("/users")
def read_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    return {"nickname": USER_DB[name]}

@app.put("/users")
def update_user(name: str, nickname: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    USER_DB[name] = nickname
    return {"status":"success"}

@app.delete("/users")
def delete_user(name: str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    del USER_DB[name]
    return {"status":"success"}