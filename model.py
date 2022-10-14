"""
File to manage databases
"""

import sqlite3
import datetime

from settings import DEBUG


class Coustomer:
    """
    TODO
    """

    def __init__(
        self,
        vehicle_no: str,
        phone_no: int,
        vehicle_type: str,
        expiry: datetime.date,
        price: int,
    ) -> None:

        self.vehicle_no = vehicle_no
        self.phone_no = phone_no
        self.vehicle_type = vehicle_type
        self.test_date = datetime.date.today()
        self.test_time = datetime.datetime.now()
        self.expiry = expiry
        self.price = price

    def __repr__(self) -> str:
        return f"{self.vehicle_no}, {self.phone_no}, {self.vehicle_type}, {self.test_date}, {self.expiry}, {self.price}"


if DEBUG:

    # If DEBUG is true, create a database in memory with a few random entries
    # else, create/connect to the existing database

    conn = sqlite3.connect(
        ":memory:", detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
    )
    print("[OK] Created test database in memory")
    # In order to execute SQL statements and fetch results from SQL queries,
    # we will need to use a database cursor. Call con.cursor() to create the Cursor:
    cursor = conn.cursor()

    # ID is automatically inserted as ROWID
    # To get ROWID you use have to explicity say it
    # eg, SELECT ROWID, * FROM cousomers
    cursor.execute(
        """
        CREATE TABLE coustomers  
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

    # creating few coustomer instace with random data
    today = datetime.date.today()
    now = datetime.datetime.now()
    e1 = datetime.date.fromisoformat("2023-10-04")
    e2 = datetime.date.fromisoformat("2023-09-05")
    e3 = datetime.date.fromisoformat("2023-09-04")
    c1 = Coustomer("kl51a0000", 1234567890, "car", e1, 130)
    c2 = Coustomer("kl51b0000", 1234567918, "bike", e2, 80)
    c3 = Coustomer("kl50a0002", 1234575986, "bike", e2, 80)
    c4 = Coustomer("kl50a0003", 1234575984, "jeep", e3, 100)

    sample_data = [
        (
            c1.vehicle_no,
            c1.phone_no,
            c1.vehicle_type,
            c1.test_date,
            c1.test_time,
            c1.expiry,
            c1.price,
        ),
        (
            c2.vehicle_no,
            c2.phone_no,
            c2.vehicle_type,
            c2.test_date,
            c2.test_time,
            c2.expiry,
            c2.price,
        ),
        (
            c3.vehicle_no,
            c3.phone_no,
            c3.vehicle_type,
            c3.test_date,
            c3.test_time,
            c3.expiry,
            c3.price,
        ),
        (
            c4.vehicle_no,
            c4.phone_no,
            c4.vehicle_type,
            c4.test_date,
            c4.test_time,
            c4.expiry,
            c4.price,
        ),
    ]

    try:
        cursor.executemany(
            """
            INSERT INTO coustomers (VEHICLE_NO, PHONE_NO, VEHICLE_TYPE, TEST_DATE, TEST_TIME, EXPIRY, PRICE) VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            sample_data,
        )
        conn.commit()

        cursor.execute("""SELECT * FROM coustomers""")
        data = cursor.fetchone()
        print(data)

        conn.close()

    except sqlite3.Error as error:
        conn.close()
        print(error)
