#!/bin/python3

import os


def compareTriplets(a, b):
    alice_points_num, bob_points_num = 0, 0
    for i, a_el in enumerate(a):
        if a_el > b[i]:
            alice_points_num += 1
        elif a_el < b[i]:
            bob_points_num += 1
    
    return [alice_points_num, bob_points_num]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
