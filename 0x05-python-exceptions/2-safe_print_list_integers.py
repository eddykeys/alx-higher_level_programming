#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    k = 0
    for k in range(x):
        try:
            print("{:d}".format(my_list[k]), end="")
            k += 1
        except (ValueError, TypeError):
            k += 1
            continue
    print("")
    return k
