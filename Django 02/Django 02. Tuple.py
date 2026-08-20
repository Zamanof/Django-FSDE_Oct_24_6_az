# tuple
# tpl = (1,)
#
# print(type(tpl))
# print(tpl)

# numb1, numb2 = 25, 6
# print(f"numb1 = {numb1}; numb2 = {numb2};")

# classic swap algorithm
# tmp = numb1
# numb1 = numb2
# numb2 = tmp

# arithmetic swap algorithm
# numb1 = numb1 + numb2
# numb2 = numb1 - numb2
# numb1 = numb1 - numb2

# python swap style (tuple)
# numb1, numb2 = numb2, numb1
#
# print(f"numb1 = {numb1}; numb2 = {numb2};")

# def summ(*args):
#     print(type(args))
#     summ = 0
#     for arg in args:
#         summ += arg
#     return summ
#
# print(summ(25, 89, 78, 9, 5))


def foo():
    return 25, 65, 5

print(type(foo()))
a, _, c = foo()
print(a, c)
