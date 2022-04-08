#!/bin/python3

import os


def diagonalDifference(arr):
    left_diag, right_diag = 0, 0
    rows_num, columns_num = len(arr), len(arr[0])
    i, j = 0, 0
    while i < rows_num and j < columns_num:
        left_diag += arr[i][j]
        right_diag += arr[i][columns_num - j - 1]
        i += 1
        j += 1
        
    return abs(left_diag - right_diag)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    fptr.write(str(result) + '\n')
    fptr.close()