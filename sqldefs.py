import psycopg2

from cfg import host, user, password, db_name


connection = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    database=db_name
)

cur = connection.cursor()


def select_vers():
    cur.execute(
        """SELECT version();"""
    )

    print(f"Version: {cur.fetchone()}")


