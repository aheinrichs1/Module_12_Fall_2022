"""
Program: test_customer_exceptions.py
Author: Alex Heinrichs
Date Created: 11/12/2022

File for testing custom exceptions
"""
import unittest
from topic2.Customer import Customer
from custom_exceptions.customer_exceptions import *


class CustomerTest(unittest.TestCase):
    def setUp(self):
        self.validCustomer = Customer(1337, "Heinrichs", "Alex", "123-123-1234")

    def tearDown(self):
        del self.validCustomer

    def test_valid_customer_id(self):
        try:
            test_cust = self.validCustomer
        except InvalidCustomerIdException:
            self.fail('test threw InvalidCustomerIdException')

    def test_invalid_customer_id(self):
        with self.assertRaises(InvalidCustomerIdException):
            c = Customer(0, "Heinrichs", "Alex", "123-123-1234")

    def test_valid_last_name(self):
        try:
            test_cust = self.validCustomer
        except InvalidNameException:
            self.fail('test threw InvalidNameIdException')

    def test_invalid_last_name(self):
        with self.assertRaises(InvalidNameException):
            c = Customer(1000, "#Heinrichs#", "Alex", "123-123-1234")

    def test_valid_first_name(self):
        try:
            test_cust = self.validCustomer
        except InvalidNameException:
            self.fail('test threw InvalidNameException')

    def test_invalid_first_name(self):
        with self.assertRaises(InvalidNameException):
            c = Customer(1237, "Heinrichs", "Al3x", "123-123-1234")

    def test_valid_phone_number_format(self):
        try:
            test_cust = self.validCustomer
        except InvalidPhoneNumberFormat:
            self.fail('test threw InvalidCustomerIdException')

    def test_invalid_phone_number_format(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            c = Customer(7854, "Heinrichs", "Alex", "1234532-121233-123423")

    def test_str(self):
        self.assertEqual(self.validCustomer.__str__(), '1337: Heinrichs, Alex Phone: 123-123-1234')
