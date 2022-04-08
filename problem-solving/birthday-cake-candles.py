#!/bin/python3

import os


def birthdayCakeCandles(candles):
    max_number = max(candles)
    return sum([1 for i in candles if i == max_number])


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
