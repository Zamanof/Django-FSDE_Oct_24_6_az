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

    def get_info(self):
        return f"{super().get_info()}. \nGroup: {self.group}"


class Foo:
    def get_info(self):
        return "Foo"


class Other:
    def get_info(self):
        return "Other"


student = Student("Ali", "Aliyev", 24, "FBMS_2_11")
human = Human("Vali", "Valiev", 30)
foo = Foo()
other = Other()

lst = [student, human, foo, other]

for item in lst:
    print(item.get_info())
    print()


# duck typing