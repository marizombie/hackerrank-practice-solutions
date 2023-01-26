#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def process(a, b):
    a_dict = {k:a.count(k) for k in a}
    b_dict = {k:b.count(k) for k in b}
    res_dict = {}
    
    for k, v in a_dict.items():
        res_dict[k] = abs(b_dict.get(k, 0) - v)
        
    for k, v in b_dict.items():
        res_dict[k] = abs(a_dict.get(k, 0) - v)
        
    return sum(i for i in res_dict.values())
    

def makeAnagram(a, b):
    # Write your code here
    if a >= b:
        res = process(a, b)
    else:
        res = process(b, a)
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
