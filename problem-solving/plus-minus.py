#!/bin/python3

def plusMinus(arr):
    arr_len = len(arr)
    positives = sum(1 for i in arr if i > 0)/arr_len
    negatives = sum(1 for i in arr if i < 0)/arr_len
    zeros = sum(1 for i in arr if i == 0)/arr_len
    print(f'{positives}\n{negatives}\n{zeros}')


if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
