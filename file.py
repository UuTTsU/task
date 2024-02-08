class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age


class DictMixin:
    def returnDict(self):
        return self.__dict__


class Student(Person, DictMixin):
    def __init__(self, university, name, surname, age):
        self.university = university
        super().__init__(name, surname, age)


student1 = Student('BTU', 'giorgi', 'utsunashvili', 19)
print(student1.university)
print(student1.name)
print(student1.surname)
print(student1.age)
print(student1.returnDict())