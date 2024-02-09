from fastapi import FastAPI
app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name":"Bar"}, {"item_name": "Baz"}]

@app.get("/items/") 
#?key=value&key=value&....
def read_item(skip: int=0, limit: int = 10):
    return fake_items_db[skip:skip+limit]

@app.get("/items/{item_id}") 
#?key=value&key=value&....
def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    #item_id = 위의 입력을 받아 사용
    #/items/sh?needy=someneed 이런식으로 needy를 추가 입력
    return item