import types

in_list: list = [1,2,3,4,5,6,6,6,7,8,9,9,9,4,4,5]

unique_list: list = list(set(in_list))

print(unique_list)