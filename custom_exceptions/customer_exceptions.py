"""
Program: customer_exceptions.py
Author: Alex Heinrichs
Date Created 11/12/2022

A python file containing custom exceptions to be tested with the customer class
"""


class InvalidCustomerIdException(Exception):
    """
    Raises error if a customer id falls outside the assigned range
    (1000-9999)
    """
    pass


class InvalidNameException(Exception):
    """
    Raises error if name doesn't contain alpha characters
    """
    pass


class InvalidPhoneNumberFormat(Exception):
    """
    Raises error if phone number is in incorrect format
    """
