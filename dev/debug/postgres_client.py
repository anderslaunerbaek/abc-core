import logging

from abc_core.database.postgress_client import PostgresSQL
from abc_core.utils.logger_client import get_basis_logger_config


def main():
    logging.basicConfig(**get_basis_logger_config())

    database: str = "test"
    host: str = "172.29.174.193"
    port: int = 54320
    user: str = "test"
    password: str = "example"

    db = PostgresSQL(
        database=database, host=host, port=port, user=user, password=password
    )

    res = db.select("SELECT * FROM test;")
    print(res)
    # for i in range(100):
    #     db.insert(
    #         query="INSERT INTO test(comment) VALUES (%s)", data=(f"private-blog{i+10}",)
    #     )
    res = db.update(
        "UPDATE test SET comment=%s WHERE id=%s;",
        (
            "value21",
            1,
        ),
    )
    res = db.select("SELECT * FROM test where id=%s", (1,))
    print(res)
    # res = db.select("SELECT * FROM test where id=%s;", (101,))
    # print(res)

    # (id text not null primary key, date text, title text, content text, public integer
    db.close_connection()


if __name__ == "__main__":
    main()
