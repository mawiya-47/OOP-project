# person.py
# Base class for every human in the hospital (patient, doctor, employee).
# It is an ABSTRACT class: it cannot be used to create objects directly.

from abc import ABC, abstractmethod


class Person(ABC):
    """Parent class holding the attributes that every person has."""

    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone

    @abstractmethod
    def get_details(self):
        """Every child class MUST write its own version of this method.
        If a child class forgets, Python refuses to create its objects.
        This forces all person types to be able to describe themselves."""
        pass
