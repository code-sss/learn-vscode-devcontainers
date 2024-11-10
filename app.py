from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_item():
    return {"message": f"Hello World!"}
