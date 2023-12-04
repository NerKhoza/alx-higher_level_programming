#!/usr/bin/python3

def element_at(my_list, idx):

    if idx < 0:
        return None

    if idx >= len(my_list):
        return None

my_list = [1, 2, 3, 4, 5]

result3 = element_at(my_list, 10)
print(result3)
