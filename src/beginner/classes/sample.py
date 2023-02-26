from student_class import Student
from person_class import Person

p = Person('iman', 'nemati', 34, 'm')
print(p)
p.save()

is_male = p.is_male()
print(is_male)

s = Student('ali', 'nemati', 39, 'm', 2009, 'software engineer', 'A')
print(s)
