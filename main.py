"""
I want a database object that can be able to do CRUD operations
something like this
"""

import datetime
import json
import logging

from model import CustomersDB

logging.basicConfig(level=logging.DEBUG)
# settings.json
with open("settings.json", "r") as file:
    settings = json.load(file)
    logging.info("Settings loaded")


class Customer:
    """
    TODO
    """

    def __init__(
        self,
        vehicle_no: str,
        name: str,
        phone_no: int,
        vehicle_type: str,
        expiry: datetime.date,
        price: int,
    ) -> None:

        self.vehicle_no = vehicle_no
        self.name = name
        self.phone_no = phone_no
        self.vehicle_type = vehicle_type
        self.test_date = datetime.date.today()
        self.test_time = datetime.datetime.now()
        self.expiry = expiry
        self.price = price

    def __repr__(self) -> str:
        return f"Customer{self.vehicle_no}, {self.phone_no}, {self.vehicle_type}, {self.test_date}, {self.expiry}, {self.price}"


def main():
    db = CustomersDB()
    # Create tables in database for the first time after installation
    if not settings["DB_INITIALIZED"]:
        db.initialize()
        settings["DB_INITIALIZED"] = True
        with open("settings.json", "w") as file:
            json.dump(settings, file)
            logging.info("Updated Settings")

    vehicle_no = input("Entter vehicle Number\t\t")
    name = input("Enter name\t\t")
    phone_no = int(input("Enter phone number\t\t"))
    vehicle_type = input("Enter vehicle type\t\t")
    expiry_day = int(input("Enter expiry day\t\t"))
    expiry_month = int(input("Enter expiry month\t\t"))
    expiry_year = int(input("Enter expiry year\t\t"))
    price = int(input("Enter price\t"))

    expiry = datetime.date(expiry_year, expiry_month, expiry_day)

    c = Customer(vehicle_no, name, phone_no, vehicle_type, expiry, price)
    print(c)
    db.insert_to_db(c)

    print(db.get_n_entry())


if __name__ == "__main__":
    main()
