#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        elem = 0
        for i in my_list:
            if elem < x:
                print("{}".format(i), end='')
                elem += 1
        print('')
        return elem
    except SyntaxError:
        print("Error Syntax")
