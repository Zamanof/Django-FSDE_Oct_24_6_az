# generators
# yield

# numbers = [i for i in range(10)]
# print(numbers)

# numbers_gen = (i for i in range(10))
# print(numbers_gen)
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))
# print(next(numbers_gen))

import datetime

def infinite_days(start = None):
    if start is None:
        start = datetime.date.today()
    while True:
        yield start
        start += datetime.timedelta(days=1)


# days = infinite_days()
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))
# print(next(days))


def read_file_lines(path:str):
    with open(path, encoding="utf-8") as f:
        for line in f:
            yield line.strip()


for line in read_file_lines("students.txt"):
    input()
    print(line)


'''
Əsas konsepsiyası:
    1. "Təmbəllik"
    2. Yaddaşa qənaət
    3. Generatorun state-i
    4. Birdəfəlik
'''