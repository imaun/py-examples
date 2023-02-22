from xmlrpc.client import Boolean


class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'

    def is_male(self) -> Boolean:
        if self.gender.lower() == 'm':
            return True
        return False
