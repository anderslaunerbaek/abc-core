
import logging

from abc_core.database.sqllite_client import SQLLite
from abc_core.utils.logger_client import get_basis_logger_config


def main():
    logging.basicConfig(**get_basis_logger_config())
    db = SQLLite(filename="../../data/application.db") 


    res = db.select("SELECT * FROM blogs1")
    print(res)

    # for i in range(1):
    #     db.insert(
    #         query="INSERT INTO blogs VALUES (?,?,?,?,?);",
    #         data=(f'private-blog{i+10}', '2021-03-07', 'Secret blog' ,'This is a secret',3)
    #     )
    # res = db.select("SELECT * FROM blogs WHERE public >= 3")
    # print(res)

    # (id text not null primary key, date text, title text, content text, public integer
    db.close_connection()
if __name__ == "__main__":
    main()
