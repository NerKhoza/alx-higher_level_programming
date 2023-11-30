#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    lenarg = len(sys.argv)

    if lenarg == 1:
        print("{} arguments.".format(lenarg - 1))
    else:
        print("{} arguments:".format(lenarg - 1))

        for i in range(1, lenarg):
            print("{} : {}".format(i, sys.argv[i]))
