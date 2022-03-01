
import logging
from abc import abstractmethod
from dataclasses import dataclass
from typing import Any, List, Optional, Tuple, Union


@dataclass
class DBCore:

    def __post_init__(self):
        self.connection = self._create_connection()

    @abstractmethod
    def _create_connection(self) -> Any:
        pass


    def close_connection(self) -> None:
        try:
            self.connection.close()
            logging.info("DB connection has been closed...")
        except Exception as msg:
            logging.error(f"Not able to close db connection. Got following msg: {msg}...")
            
    def __enter__(self):
        logging.info("Calling __enter__")
        return self.connection.cursor()

    def __exit__(self, error: Exception, value: object, traceback: object):
        logging.info("Calling commit and __exit__")
        self.connection.commit()


    def _check_query(self, query:str) -> str:
        _end_sign: str = ";"
        if not query.endswith(_end_sign):
            logging.warning(f"Added > {_end_sign} < to the end of the query: {query}.")  
            query = f"{query}{_end_sign}" 
        return query

    def select(self, query: str, data: tuple[Any, ...] = None) -> Optional[List[Tuple[Any, ...]]]:
        query = self._check_query(query)
        with self as cursor:
            try:
                logging.info(f"Calling select query: {query}")
                cursor.execute(query, data)
                return cursor.fetchall()
            except Exception as msg:
                logging.error(f"Error for select query: {query} with following msg: {msg}...")

    def insert(self, query: str, data: tuple[Any, ...]) -> bool:
        query = self._check_query(query)
        with self as cursor:
            try:
                logging.info(f"Calling insert query: {query}")
                cursor.execute(query, data)
                return True
            except Exception as msg:
                logging.error(f"Error for insert query: {query} with following msg: {msg}...")
                self.connection.rollback()
                return False

    def update(self, query: str, data: tuple[Any,...]) -> bool:
        query = self._check_query(query)
        with self as cursor:
            try:
                logging.info(f"Calling update query: {query}")
                cursor.execute(query, data)
                return True
            except Exception as msg:
                logging.error(f"Error for update query: {query} with following msg: {msg}...")
                self.connection.rollback()
                return False



def main():
    db = DBCore() 
    db.close_connection()

if __name__ == "__main__":
    main()
