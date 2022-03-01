
import logging
from dataclasses import dataclass

from mysql.connector import MySQLConnection, connect

from .core_client import DBCore


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
