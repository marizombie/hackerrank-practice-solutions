#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#
def find_a(substring):
    a_number = 0
    for letter in substring:
        if letter == 'a':
            a_number += 1
    return a_number

def repeatedString(s, n):    
    matches = find_a(s)
    pattern_len = len(s)
    repetitions = n // pattern_len
    remnant_len = n - repetitions * pattern_len
    remnant_matches = find_a(s[:remnant_len]) 
    
    return matches * repetitions + remnant_matches

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()

# 'abc' 10