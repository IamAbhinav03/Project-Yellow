"""
I want a database object that can be able to do CRUD operations
something like this
"""

import datetime

from model import CoustomersDB as db

settings = {}  # settings.json


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

    def __repr__(self):
        return f"{self.vehicle_no}, {self.phone_no}, {self.vehicle_type}, {self.test_date}, {self.expiry}, {self.price}"


def main():
    pass


if __name__ == "main.py":
    main()
