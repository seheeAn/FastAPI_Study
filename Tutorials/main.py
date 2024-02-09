from fastapi import FastAPI
app = FastAPI()

# Path Operation이 수행되었을 때 호출될 python 함수
@app.get("/") #URL 에서 첫 번째 / 부터 시작되는 마지막 부분.
def read_root():
    return {"Hello": "World"}
