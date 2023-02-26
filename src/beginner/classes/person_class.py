import json

class Person:
    def __init__(self, fname, lname, age, gender):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        return f'{self.fname} {self.lname}'

    def is_male(self) -> bool:
        if self.gender.lower() == 'm':
            return True
        return False


    def save(self):
        content = json.dumps(vars(self))
        with open(self.fname + '.json', 'w', encoding='utf-8') as f:
            f.write(content)
