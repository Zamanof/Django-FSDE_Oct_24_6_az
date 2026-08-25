class Human:
    # class attribute -> static field-lərin analoqu
    # name = 'Nadir'
    # surname = 'Zamanov'
    __count = 0
    def __init__(self, name, surname, age):
        self.name = name            # public
        self._surname = surname     # protected
        self.__age = age            # private
        Human.__count += 1

    @staticmethod
    def get_count():
        return Human.__count

    @classmethod
    def get_my_count(cls):
        return cls.__count


    # def initialize(self, name, surname):
    #     Human.name = name
    #     Human.surname = surname



print(Human.get_my_count())
human = Human("Nadir", "Zamanov", 45)
print(human.name)
# print(human._surname)
# print(human._Human__age)
print(human.get_count())

human1 = Human("Salam", "Salamazade", 54)
print(human1.name)
print(Human.get_count())


