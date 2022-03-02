import logging

from abc_core.database.mysql_client import MySQL
from abc_core.utils.logger_client import get_basis_logger_config


def main():
    logging.basicConfig(**get_basis_logger_config())

    database: str = "test"
    host: str = "172.31.220.220"
    port: int = 33060
    user: str = "root"
    password: str = "root"

    db = MySQL(database=database, host=host, port=port, user=user, password=password)

    # res = db.select("SELECT * FROM test")
    # print(res)
    # for i in range(100):
    #     db.insert(
    #         query="INSERT INTO test(comment) VALUES (%s)",
    #         data=(f'private-blog{i+10}',)
    #     )
    res = db.update(
        "UPDATE test SET comment=%s WHERE id=%s;",
        (
            "value21",
            101,
        ),
    )
    res = db.select("SELECT * FROM test where id=101")
    print(res)
    res = db.select("SELECT * FROM test where id=%s;", (101,))
    print(res)

    # (id text not null primary key, date text, title text, content text, public integer
    db.close_connection()


if __name__ == "__main__":
    main()
