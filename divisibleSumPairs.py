import os

def divisibleSumPairs(n ,k, ar):
    count = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if ((ar[i] + ar[j])%k == 0):
                count += 1
    return count
if __name__ == '__main__':
    fptr = open("input.txt",'r')
    first_multiple_input = fptr.readline().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    ar =  list(map(int, fptr.readline().rstrip().split()))
    result = divisibleSumPairs(n, k, ar)
    
    fptr.close()
    fptr = open("output.txt", 'w')

    fptr.write(str(result) + '\n')
    fptr.close()