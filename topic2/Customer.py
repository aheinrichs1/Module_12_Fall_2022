"""
Program: Customer.py
Author: Alex Heinrichs
Date Created: 11/02/2022
Date Modified: 11/12/2022

Contains a Customer class and driver code for practice with classes
Modified for validation, custom exception and testing practice
"""
from custom_exceptions import *


class Customer:
    def __init__(self, cid, lname, fname, pnumber):
        # validates that customer id is an int between 1000 and 9999
        try:
            # if cid is a string this will raise error
            if cid < 1000 or cid > 9999:
                raise InvalidCustomerIdException
        # if cid is a string this error will be raised
        except ValueError:
            raise InvalidCustomerIdException
        self.customer_id = cid
        # validates last and first name contain only alpha numbers
        # create a set of accepted characters
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise InvalidNameException
        self.last_name = lname
        self.first_name = fname
        # validates phone number is in format 123-456-7890
        try:
            if len(pnumber) != 12 or pnumber[3] != '-' or pnumber[7] != '-':
                raise InvalidPhoneNumberFormat
        except InvalidPhoneNumberFormat:
            raise InvalidPhoneNumberFormat
        self.phone_number = pnumber

    def display(self):
        return self.customer_id + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number + " Address: " + self.address

    def __str__(self):
        return str(self.customer_id) + ": " + self.last_name + ", " + self.first_name + " Phone: " + self.phone_number

    def __repr__(self):
        return 'Customer({},{},{},{},{})'.format(self.customer_id, self.last_name, self.first_name, self.phone_number)


# driver
if __name__ == "__main__":
    try:
        customer = Customer(999, "Heinrichs", "Alex", "123-123-1234")
    except InvalidCustomerIdException:
        print('Invalid customer id exception test passed')

    try:
        customer = Customer(1234, "Master Heinrichs", "Alex", "123-123-1234")
    except InvalidNameException:
        print('Invalid last name exception test passed')

    try:
        customer = Customer(5678, "Heinrichs", "MC Alex", "123-123-1234")
    except InvalidNameException:
        print('Invalid first name exception test passed')

    try:
        customer = Customer(9000, "Heinrichs", "Alex", "1-123-123-1234")
    except InvalidPhoneNumberFormat:
        print('Invalid phone number exception test passed')
