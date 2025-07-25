# initial hello world Flask app

import os
import uuid

import psycopg2
from flask import Flask, jsonify, request

app = Flask(__name__)

DATABASE_URI = os.environ.get("POSTGRESQL_DB_CONNECT_STRING", "")


@app.route("/")
def index():
    return "Hello, world!\n"


def fibonacci(n):
    if n < 0:
        raise ValueError("Invalid input")
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


@app.route("/fibonacci/<int:n>", methods=["GET"])
def get_fibonacci(n):
    if n < 0:
        return jsonify({"error": "Invalid input"}), 400
    return jsonify({"fibonacci": fibonacci(n)})


@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"}), 200


def get_connection():
    return psycopg2.connect(DATABASE_URI)


@app.route("/keys", methods=["POST"])
def create_key():
    data = request.get_json()
    value = data.get("value")

    if not value:
        return jsonify({"error": "Value is required"}), 400

    key_id = uuid.uuid4()  # Generate UUID on the server side

    with get_connection() as conn, conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO secret_keys (id, value) VALUES (%s, %s);
            """,
            (str(key_id), value),  # Convert UUID to string
        )
        conn.commit()

    return jsonify({"key_id": str(key_id)}), 201


@app.route("/keys/<key_id>", methods=["GET"])
def get_key(key_id):
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
                return jsonify({"key_id": str(result[0]), "value": result[1]})
            else:
                return jsonify({"error": "Key not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run()
