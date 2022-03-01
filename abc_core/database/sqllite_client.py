
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
