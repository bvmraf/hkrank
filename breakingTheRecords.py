#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    m = l = scores[0]
    cm = cl = 0
    for i in range(1, n):
        if m < scores[i]:
            m = scores[i]
            cm += 1
        if l > scores[i]:
            l = scores[i]
            cl += 1
    return [cm, cl]
if __name__ == '__main__':
    fptr = open("input.txt", 'r')

    n = int(fptr.readline().strip())

    scores = list(map(int, fptr.readline().rstrip().split()))

    result = breakingRecords(scores)
    fptr.close()

    fptr = open("output.txt", 'w')
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
