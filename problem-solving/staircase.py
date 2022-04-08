#!/bin/python3

def staircase(n):
    char = '#'
    for i in range(1, n + 1):
        print((char*i).rjust(n))


if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
