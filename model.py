"""
File to manage databases
"""

from . import settings
import sqlite3

if settings.DEBUG:
	"""
	If DEBUG is true, create a database in memory with a few random entries
	else, create/connect to the existing database
	"""
	pass
