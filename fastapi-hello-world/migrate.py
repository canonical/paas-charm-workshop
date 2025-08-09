import os
import uuid

import psycopg2

DATABASE_URI = os.environ["POSTGRESQL_DB_CONNECT_STRING"]


def migrate():
    with psycopg2.connect(DATABASE_URI) as conn, conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS secret_keys (
                id UUID PRIMARY KEY,
                value TEXT NOT NULL
            );
            INSERT INTO secret_keys (id, value) VALUES ('e53a48d1-b45f-4398-a114-b14c7caa672d', 'Donnez-moi un biscuit sil vous plait');
            """
        )
        conn.commit()


if __name__ == "__main__":
    migrate()
