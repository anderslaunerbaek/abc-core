
import logging
from dataclasses import dataclass
from typing import Any

from mysql.connector import MySQLConnection, connect

from core_client import DBCore


@dataclass
class MySQL(DBCore):
    database: str
    host: str
    port: int
    user: str
    password: str

    def _create_connection(self) -> MySQLConnection:
        
        logging.info("Calling _create_connection")
        return connect(
            database = self.database, 
            host = self.host, 
            port = self.port, 
            user = self.user, 
            password = self.password,
            # TODO
            auth_plugin='mysql_native_password'
            )

def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s.%(msecs)03d:%(levelname)s:%(module)s:%(funcName)s:%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
    )

    database: str = "test"
    host: str = "172.31.220.220"
    port: int = 33060
    user: str = "root"
    password: str = "root"

    db = MySQL(
        database = database,
        host= host, 
        port=port, 
        user=user,
        password = password) 


    # res = db.select("SELECT * FROM test")
    # print(res)
    # for i in range(100):
    #     db.insert(
    #         query="INSERT INTO test(comment) VALUES (%s)",
    #         data=(f'private-blog{i+10}',)
    #     )
    res = db.update("UPDATE test SET comment=%s WHERE id=%s;", ("value21",101,))
    res = db.select("SELECT * FROM test where id=101")
    print(res)
    res = db.select("SELECT * FROM test where id=%s;", (101,))
    print(res)

    # (id text not null primary key, date text, title text, content text, public integer
    db.close_connection()

if __name__ == "__main__":
    main()
