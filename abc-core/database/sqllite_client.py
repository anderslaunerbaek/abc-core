
import logging
import sqlite3
from dataclasses import dataclass

from .core_client import DBCore


@dataclass
class SQLLite(DBCore):
    filename: str

    def _create_connection(self) -> sqlite3.Connection:
        
        logging.info("Calling _create_connection")
        if self.filename is None:
            logging.error("Unkown filename")
        return sqlite3.connect(self.filename)

def main():
    logging.basicConfig(level=logging.INFO)
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
