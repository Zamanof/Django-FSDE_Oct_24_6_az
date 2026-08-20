# LEGB
# Local
# Enclosing
# Global
# Built-in

from math import pi as PI

print(f"Built-in PI = {PI}")

def outer():
    # global PI
    PI = "Salam"
    def inner():
        # nonlocal PI
        PI = True
        print(f"Local PI = {PI}")
    inner()
    print(f"Enclosing PI = {PI}")


PI = -56
print(f"Global PI = {PI}")
outer()

# pure function, closure, generators, decorators
