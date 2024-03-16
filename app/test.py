from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def star():
    return {"responce":"hola mundo"}