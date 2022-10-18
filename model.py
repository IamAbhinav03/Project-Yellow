"""
File to manage databases
"""

import sqlite3
import logging


class CustomersDB:
    def __init__(self, test: bool = False) -> None:
        pass

    def initialize(self):
        logging.debug("Intializing CustomersDB")
        try:
            conn = sqlite3.connect(
                "customers.db",
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
            )
            logging.info("Created Database")
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE customers
                (VEHICLE_NO TEXT NOT NULL,
                NAME TEXT NOT NULL,
                PHONE_NO INT NOT NULL, 
                VEHICLE_TYPE TEXT NOT NULL, 
                TEST_DATE date NOT NULL, 
                TEST_TIME timestamp NOT NULL, 
                EXPIRY date NOT NULL, 
                PRICE INT NOT NULL)
                """
            )
            logging.info("Inserted tables to the db")
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            logging.critical(f"Could not connect to database\n{error}")

    def _connect(self, db_name: str = "customers.db") -> sqlite3.Connection | None:
        """
        Starts a connection to the production database coustomers.db
        Args:
            test (bool): If true, creates a in-memory database an connects to it
        Returns:
            On succesful execution returns
                conn (Connection object)
                cursor (Cursor object to the db)
            else returns
                None
        """
        try:
            conn = sqlite3.connect(
                database=db_name,
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
            )
            logging.info(f"Succefully connected to {db_name}")

        except sqlite3.Error as error:
            logging.critical(error)
            conn = None

        return conn

    def insert_to_db(self, customer):
        """
        Insert a coustomer record to the database
        Args:
            coustomer: An instance of coustomer object that needs to be stored
            test (bool): If true, the operation will be executed in the test database
        """

        conn = self._connect()
        if conn:
            cursor = conn.cursor()
            try:
                with conn:
                    cursor.execute(
                        """
                        INSERT INTO customers (
                            VEHICLE_NO, NAME, PHONE_NO, VEHICLE_TYPE, 
                            TEST_DATE, TEST_TIME, EXPIRY, 
                            PRICE) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                        """,
                        (
                            customer.vehicle_no,
                            customer.name,
                            customer.phone_no,
                            customer.vehicle_type,
                            customer.test_date,
                            customer.test_time,
                            customer.expiry,
                            customer.price,
                        ),
                    )
                    logging.debug("Insertion succesfull")
                    logging.debug("Clossing Connection")
            except sqlite3.Error as error:
                logging.critical(error)

            conn.close()

    def update_db_entry(self):
        pass

    def get_n_entry(self, n: int = 1) -> list | None:
        """
        Fetches first n enties from the database
        Args:
            - n (int) : Number of entries to be fetched, default n = 1
        Return
            - t (list) : list of fetched data
        """
        conn = self._connect()
        if conn:
            cursor = conn.cursor()
            with conn:
                cursor.execute("""SELECT * FROM customers""")
                if n == 1:
                    t = cursor.fetchone()
                    logging.info("Fetch first entry from db")
                else:
                    t = cursor.fetchmany(n)
                    logging.info(f"Fetched first {n} entries from db")

            conn.close()
            return t


def main():
    pass


if __name__ == "__main__":
    main()
