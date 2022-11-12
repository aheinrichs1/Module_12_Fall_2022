"""
Program: abstract_class_assignment.py
Author: Alex Heinrichs
Date Created: 11/12/2022

Contains an abstract class Rider and subclasses Bicycle, Motorcycle,
and Car that implements the abstract methods
"""
from abc import ABC, abstractmethod


class Rider(ABC):
    @abstractmethod
    def ride(self):
        pass

    @abstractmethod
    def riders(self):
        pass


class Bicycle(Rider):
    def ride(self):
        print('Human powered, not enclosed')

    def riders(self):
        print('1 or 2 if tandem or a daredevil')


class Motorcycle(Rider):
    def ride(self):
        print('Engine powered, not enclosed')

    def riders(self):
        print('1 or 2')


class Car(Rider):
    def ride(self):
        print('Engine powered, enclosed')

    def riders(self):
        print('1 plus comfortably')


# driver code
if __name__ == '__main__':
    # create objects from subclasses
    b = Bicycle()
    m = Motorcycle()
    c = Car()

    # Bicycle functions
    b.ride()
    b.riders()

    # print new line
    print()

    # Motorcycle functions
    m.ride()
    m.riders()

    # print new line
    print()

    # Car functions
    c.ride()
    c.riders()
