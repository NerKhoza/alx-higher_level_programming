#!/usr/bin/python3
def uppercase(str):
    for itr in str:
        temp = itr
        if ord(temp) >= 97 and ord(temp) <= 122:
            temp = chr(ord(itr) - 32)
        print("{}".format(temp), end="")
    print()
