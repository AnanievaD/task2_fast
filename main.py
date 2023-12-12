from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def f_index():
    return {"Самосватова Дарья Андреевна"}

@app.get('/tools')
async def f_indexT():
    return "Низкий навык в программировании"

@app.get('/users')
async def f_indexU():
    return "+79564363894"