from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}

# http://127.0.0.1:8000/items/101
# > {"item_id":101} 출력