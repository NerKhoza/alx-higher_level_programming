#!/usr/bin/python3
if __name__ == "__main__":

    import sys
    lenArg = len(sys.argv)

    if lenArg == 1:
        print("{} arguments.".format(lenArg - 1))
    elif lenArg == 2:
        print("{} argument.".format(lenArg - 1))
    else:
        print("{} arguments:".format(lenArg - 1))
    for i in range(1, lenArg):
            print("{}: {}".format(i, sys.argv[i]))
