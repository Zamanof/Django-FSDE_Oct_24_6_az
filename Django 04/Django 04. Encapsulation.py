class Human:
    __count = 0
    def __init__(self, name, surname, age):
        self.name = name                                 # public
        self._surname = surname                         # protected
        self.__age = age if age > 0 else 0              # private

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age if age > 0 else 0


human = Human("Nadir", "Zamanov", 45)
print(human.age)
human.age = 25
print(human.age)
