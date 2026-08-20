# list
# lst = []
# lst = list()
#
# print(lst)

lst = [25, 98, 15, 52, -45, -9, 13]

# shallow copy
# lst1 = lst

# deep copy v1
# lst1 = []
# for i in lst:
#     lst1.append(i)

# # deep copy v2
# lst1 = lst.copy()

# deep copy v3
# import copy
# lst1 = copy.copy(lst)


# deep copy v4
lst1 = lst[:]


print(lst)
print(lst1)

print()

lst1[0] = 68

print(lst)
print(lst1)

# slice
# print(lst[1:5])
# print(lst[1:5:2])
# print(lst[:5])
# print(lst[1:])
# print(lst[::-1])
# print(lst[:])