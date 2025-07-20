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
            """
        )
        conn.commit()


if __name__ == "__main__":
    migrate()
