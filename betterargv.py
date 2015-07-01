#!/usr/bin/python3

import sys

def args():
    args = []
    argv = sys.argv

    for counter, arg in enumerate(argv):
        if arg[:1] != '-' :
            # if this arg is a value, skip it
            continue
        elif (counter < len(argv) - 2) and (argv[counter + 1][:1] != '-'):
            # if this arg has a value, return a tuple of (arg, value)
            newArg = (arg, argv[counter + 1])
        else:
            # if this is a flag, return it by itself
            newArg = (arg, '')

        args.append(newArg)

    return args

# run if not being imported as model
if __name__ == "__main__":
    print(args())
