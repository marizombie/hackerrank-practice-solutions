#!/bin/python3

import os


def timeConversion(s):
    day_part = s[-2:]
    hours = int(s[:2])
    
    if hours == 12 and day_part == 'AM':
        hours = 0
    elif day_part == 'PM' and hours != 12:
        hours += 12
    
    res_string = str(hours).rjust(2, '0') + s[2:-2]
    return res_string


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
