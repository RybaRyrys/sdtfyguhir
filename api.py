from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class Doll(BaseModel):
    name: str
    brand: str
    company: str
    price: float


@app.get("/doll")
def view_doll():
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("SELECT * FROM ads")
    doll = c.fetchall()

    conn.close()

    return {"doll": doll}


@app.post("/doll")
def add_doll(doll: Doll):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("INSERT INTO doll (name, brand, company, price) VALUES (?, ?, ?, ?)",
              (doll.name, doll.brand, doll.company, doll.price))

    conn.commit()
    conn.close()

    return {"message": "Кукла добавлена"}


@app.put("/doll/{doll_id}")
def update_price(doll_id: int, new_price: float):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("UPDATE doll SET price = ? WHERE id = ?", (new_price, doll_id))

    conn.commit()
    conn.close()

    return {"message": "Цена изменена"}


@app.delete("/doll/{doll_id}")
def delete_doll(doll_id: int):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("DELETE FROM doll WHERE id = ?", doll_id)

    conn.commit()
    conn.close()

    return {"message": "Кукла удалена"}


@app.get("/doll/{name}")
def find_ad(name: str):
    conn = sqlite3.connect('newdb.db')
    c = conn.cursor()

    c.execute("SELECT * FROM doll WHERE name = ?", name)
    doll = c.fetchone()

    conn.close()

    if doll:
        return {"doll": doll}
    else:
        return {"message": "Кукла не найдена"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)