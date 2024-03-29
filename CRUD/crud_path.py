from fastapi import FastAPI, HTTPException

# create a FastAPI instance
app = FastAPI()

# user database
USER_DB = {}

# fail response
NAME_NOT_FOUND = HTTPException(status_code=400, detail="Name not found.") #에러

@app.post("/users/name/{name}/nickname/{nickname}")
def create_user(name:str, nickname:str ):
    USER_DB[name] = nickname
    return {"status" : "success"}

@app.get("/users/name/{name}")
def read_user(name:str):
    if name not in USER_DB: #예외처리
        raise NAME_NOT_FOUND
    return {"nickname": USER_DB[name]}

@app.put("/users/name/{name}/nickname/{nickname}")
def update_user(name:str, nickname:str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    USER_DB[name] = nickname
    return {"status":"success"}

@app.delete("/users/name/{name}")
def delete_user(name:str):
    if name not in USER_DB:
        raise NAME_NOT_FOUND
    del USER_DB[name]
    return {"status": "success"}

