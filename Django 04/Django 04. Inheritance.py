# C++       -> Parent class, Child class
# C#        -> Base class, Derived class
# Python    -> Super class, Subclass
class Human:
    foo = "Salam"
    def __init__(self, name, surname, age):
        self.name = name                                 # public
        self._surname = surname                         # protected
        self.__age = age if age > 0 else 0

    def get_info(self):
        return f"Name: {self.name}\nSurname: {self._surname}\nAge: {self.__age}"

    @staticmethod
    def get_foo_static_method():
        return Human.foo

    @classmethod
    def get_foo_class_method(cls):
        return cls.foo

class Student(Human):
    def __init__(self, name, surname, age, group):
        super().__init__(name, surname, age)
        self.group = group


# print(Human.get_foo_class_method())     # Salam
# print(Human.get_foo_static_method())    # Salam
# Student.foo = "Hi"
# print(Student.get_foo_static_method())    # Salam
# print(Student.get_foo_class_method())     # Salam


human = Human("Nadir", "Zamanov", 45)

student = Student("Salam", "Zamanov", 45, "group 1")

# print(isinstance(student, Student))
# print(isinstance(student, Human))
# print(isinstance(student, object))