from person_class import Person


class Student(Person):

    def __init__(self, fname, lname, age, gender, enter_year, branch, grade):
        super().__init__(fname, lname, age, gender)
        self.enter_year = enter_year
        self.branch = branch
        self.grade = grade

    def __str__(self) -> str:
        return f'{self.fname} {self.lname} {self.age}'
