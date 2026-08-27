# magic methods
class Human:
    foo = "Salam"
    def __init__(self, name, surname, age):
        self.name = name
        self._surname = surname
        self.age = age if age > 0 else 0

    def __repr__(self):
        return "Human"

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.age > other.age

    def __add__(self, other):
        return self.age + other.age

    def __int__(self):
        return self.age





human = Human("Vali", "Valiev", 25)
human1 = Human("Vali", "Valiev", 30)

# print(human)
# print(human1)

# print(human1 == human)
# print(human1 > human)
# print(human1 + human)
print(int(human1))

print(len(human))


