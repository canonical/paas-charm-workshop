import os
import uuid

import psycopg2
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

DATABASE_URI = os.environ["POSTGRESQL_DB_CONNECT_STRING"]

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


def fibonacci(n: int):
    if n < 0:
        raise ValueError("Invalid input")
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


@app.get("/fibonacci/{n}")
async def get_fibonacci(n: int):
    if n < 0:
        raise HTTPException(status_code=400, detail="Invalid input")
    return {"fibonacci": fibonacci(n)}


class SecretKey(BaseModel):
    value: str


def get_connection():
    return psycopg2.connect(DATABASE_URI)


@app.post("/keys", response_model=dict)
async def create_key(key: SecretKey):
    key_id = uuid.uuid4()  # Generate UUID on the server side

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO secret_keys (id, value) VALUES (%s, %s);
            """,
            (str(key_id), key.value),  # Convert UUID to string
        )
        conn.commit()

    return JSONResponse(content={"key_id": str(key_id)}, status_code=201)


@app.get("/keys/{key_id}", response_model=dict)
async def get_key(key_id: str):
    try:
        with get_connection() as conn, conn.cursor() as cur:
            cur.execute(
                """
                SELECT id, value FROM secret_keys WHERE id = %s;
                """,
                (key_id,),  # Convert string to UUID for querying
            )
            result = cur.fetchone()
            if result:
                return {"key_id": str(result[0]), "value": result[1]}
            else:
                raise HTTPException(status_code=404, detail="Key not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
