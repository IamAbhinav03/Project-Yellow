"""
File to manage databases
"""

import sqlite3
import logging


class CoustomersDB:
    def __init__(self, test: bool = False) -> None:
        self._initialize()
        return None

    def _initialize(self):
        logging.debug("Intializing CoustomersDB")
        try:
            conn = sqlite3.connect(
                "Coustomers.db",
                detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES,
            )
            logging.info("Created Database")
            cursor = conn.cursor()
            cursor.execute(
                """CREATE TABLE [IF NOT EXISTS] coustomers  
                (VEHICLE_NO TEXT NOT NULL,
                PHONE_NO INT NOT NULL, 
                VEHICLE_TYPE TEXT NOT NULL, 
                TEST_DATE date NOT NULL, 
                TEST_TIME timestamp NOT NULL, 
                EXPIRY date NOT NULL, 
                PRICE INT NOT NULL)
                """
            )
            conn.commit()
            conn.close()
        except sqlite3.Error as error:
            logging.critical(f"Could not connect to database\n{error}")

    def _connect(self, db_name: str):
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
                db_name, detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
            )
            logging.debug(f"Succefully connected to {db_name}")

        except sqlite3.Error as error:
            logging.critical(error)
            conn = None

        return conn

    def _insert_to_db(self, coustomer):
        """
        Insert a coustomer record to the database
        Args:
            coustomer: An instance of coustomer object that needs to be stored
            test (bool): If true, the operation will be executed in the test database
        """

        conn = self._connect("Coustomers.db")
        if conn:
            with conn:
                cursor.execute(
                    """
                    INSERT INTO coustomers (
                        VEHICLE_NO, PHONE_NO, VEHICLE_TYPE, 
                        TEST_DATE, TEST_TIME, EXPIRY, 
                        PRICE) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        coustomer.vehicle_no,
                        coustomer.phone_no,
                        coustomer.vehicle_type,
                        coustomer.test_date,
                        coustomer.test_time,
                        coustomer.expiry,
                        coustomer.price,
                    ),
                )
            logging.debug("Insertion succesfull")
            logging.debug("Clossing Connection")
            conn.close()


# if DEBUG:

#     # If DEBUG is true, create a database in memory with a few random entries
#     # else, create/connect to the existing database
#     conn, cursor = connect(test=DEBUG)
#     if conn:
#         with conn:
#             # ID is automatically inserted as ROWID
#             # To get ROWID you use have to explicity say it
#             # eg, SELECT ROWID, * FROM cousomers
#             cursor.execute(
#                 """
#                 CREATE TABLE coustomers
#                 (VEHICLE_NO TEXT NOT NULL,
#                 PHONE_NO INT NOT NULL,
#                 VEHICLE_TYPE TEXT NOT NULL,
#                 TEST_DATE date NOT NULL,
#                 TEST_TIME timestamp NOT NULL,
#                 EXPIRY date NOT NULL,
#                 PRICE INT NOT NULL)
#                 """
#             )

#     # conn = sqlite3.connect(
#     #     ":memory:", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
#     # )
#     # logging.debug("[OK] Created test database in memory")
#     # In order to execute SQL statements and fetch results from SQL queries,
#     # we will need to use a database cursor. Call con.cursor() to create the Cursor:
#     cursor = conn.cursor()

#     # ID is automatically inserted as ROWID
#     # To get ROWID you use have to explicity say it
#     # eg, SELECT ROWID, * FROM cousomers
#     cursor.execute(
#         """
#         CREATE TABLE coustomers
#         (VEHICLE_NO TEXT NOT NULL,
#         PHONE_NO INT NOT NULL,
#         VEHICLE_TYPE TEXT NOT NULL,
#         TEST_DATE date NOT NULL,
#         TEST_TIME timestamp NOT NULL,
#         EXPIRY date NOT NULL,
#         PRICE INT NOT NULL)
#         """
#     )

#     conn.commit()

#     # creating few coustomer instace with random data
#     today = datetime.date.today()
#     now = datetime.datetime.now()
#     e1 = datetime.date.fromisoformat("2023-10-04")
#     e2 = datetime.date.fromisoformat("2023-09-05")
#     e3 = datetime.date.fromisoformat("2023-09-04")
#     coustomer = Coustomer("kl51a0000", 1234567890, "car", e1, 130)
#     c2 = Coustomer("kl51b0000", 1234567918, "bike", e2, 80)
#     c3 = Coustomer("kl50a0002", 1234575986, "bike", e2, 80)
#     c4 = Coustomer("kl50a0003", 1234575984, "jeep", e3, 100)

#     sample_data = [
#         (
#             coustomer.vehicle_no,
#             c1.phone_no,
#             c1.vehicle_type,
#             c1.test_date,
#             c1.test_time,
#             c1.expiry,
#             c1.price,
#         ),
#         (
#             c2.vehicle_no,
#             c2.phone_no,
#             c2.vehicle_type,
#             c2.test_date,
#             c2.test_time,
#             c2.expiry,
#             c2.price,
#         ),
#         (
#             c3.vehicle_no,
#             c3.phone_no,
#             c3.vehicle_type,
#             c3.test_date,
#             c3.test_time,
#             c3.expiry,
#             c3.price,
#         ),
#         (
#             c4.vehicle_no,
#             c4.phone_no,
#             c4.vehicle_type,
#             c4.test_date,
#             c4.test_time,
#             c4.expiry,
#             c4.price,
#         ),
#     ]

#     try:
#         cursor.executemany(
#             """
#             INSERT INTO coustomers (VEHICLE_NO, PHONE_NO, VEHICLE_TYPE, TEST_DATE, TEST_TIME, EXPIRY, PRICE) VALUES (?, ?, ?, ?, ?, ?, ?)
#             """,
#             sample_data,
#         )
#         conn.commit()

#         cursor.execute("""SELECT * FROM coustomers""")
#         data = cursor.fetchone()
#         print(data)

#         conn.close()

#     except sqlite3.Error as error:
#         conn.close()
#         print(error)
