"""
File to manage databases
"""

from settings import DEBUG
import sqlite3
import datetime

if DEBUG:
	"""
	If DEBUG is true, create a database in memory with a few random entries
	else, create/connect to the existing database
	"""
	conn = sqlite3.connect(":memory")
	print("[OK] Created test database in memory")
	# In order to execute SQL statements and fetch results from SQL queries, 
	# we will need to use a database cursor. Call con.cursor() to create the Cursor:
	cursor = conn.cursor()

	conn.execute("""CREATE TABLE coustomer
		(ID INT PRIMARY KEY NOT NULL,
		VEHICLE_NO TEXT NOT NULL,
		PHONE_NO INT NOT NULL,
		TYPE TEXT NOT NULL,
		TEST_DATE DATE NOT NULL,
		TEST_TIME TIMESTAMP NOT NULL,
		EXPIRY DATE NOT NULL
		""")

	today = datetime.date.today()
	now = datetime.datetime.now()
	expiry = datetime.date.fromisoformat("2023-10-04")

	cursor.execute("""INSERT INTO coustomer
		(ID, VEHICLE_NO, PHONE_NO,
		TYPE, TEST_DATE, TEST_TIME,
		EXPIRY)
		VALUES (?, ?, ?, ?, ?, ?, ?)""",
		(1, "kl51k0000", 1234567890, 
		"JEEP", today, now, expiry))

	cursor.execute("""SELECT * FROM coustomer""")
	data = cursor.fetchall()
	print(data)


