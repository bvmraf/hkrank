#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#
def lcm(a, b):
    while (b%a!=0):
        t = a
        a = b%a
        b = t
    return a
def gcd(a, b):
    return int((a*b)/lcm(a,b))
def getTotalX(a, b):
    # Write your code here
    l = a[0]
    g = b[0]
    for i in range(1, n):
        l = gcd(l, a[i])
    for i in range(1, m):
        g = lcm(g, b[i])
    count = 0
    i = 1
    while l*i<=g:
        if g%(l*i)==0:
            count+=1
        i+=1
    return count
if __name__ == '__main__':
    fptr = open("input.txt", 'r+')

    first_multiple_input = fptr.readline().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, fptr.readline().rstrip().split()))

    brr = list(map(int, fptr.readline().rstrip().split()))

    fptr.close()
    total = getTotalX(arr, brr)

    fptr = open("output.txt",'w')
    fptr.write(str(total) + '\n')
    fptr.close()