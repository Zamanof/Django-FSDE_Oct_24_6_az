# dictionary - class 'dict' (C++ - map, C# - Hashtable, Dictionary<TKey, TValue>)
# dct = {}
# dct = dict()
#
# print(type(dct))



dct = {
    15: "Salam",
    15.6: "Saqol",
    "key": [25, 65],
    True: 63.5,
    (41, 6): "Hi"
}

# print(dct)

# print(dct.keys())
# print(dct.values())
print(dct.items())

for k in dct.keys():
    print(f"{k}: {dct[k]}", end=" ")
print()

for v in dct.values():
    print(f"{v}", end=" ")
print()


for k, v in dct.items():
    print(f"{k}: {v}", end=" ")
print()

def foo(**kwargs):
    print(type(kwargs))

foo(cpp = 15, python = "python")

