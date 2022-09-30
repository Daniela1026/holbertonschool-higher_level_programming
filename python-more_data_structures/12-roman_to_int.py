#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    converts = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 
            'D': 500, 'M': 1000}
    romannum = 0
    for i in range(len(roman_string)):
        if i > 0 and converts[roman_string[i]] > converts[roman_string[i - 1]]:
            romannum += converts[roman_string[i]] - 2 * \
                        converts[roman_string[i - 1]]
        else:
            romannum += converts[roman_string[i]]
    return romannum
