import logging
from dataclasses import dataclass
from typing import Any

import psycopg2

from .core_client import DBCore


@dataclass
class PostgresSQL(DBCore):
    database: str
    host: str
    port: int
    user: str
    password: str

    def _create_connection(self) -> Any:

        logging.info("Calling _create_connection")
        return psycopg2.connect(
            database=self.database,
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
        )
