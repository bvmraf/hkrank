import os

def birthday(s, d, m):
    sm = count = 0
    for i in range(m):
        sm  += s[i]
    if sm == d:
        count += 1
    for i in range(m, n):
        sm += s[i]
        sm -= s[i-m]
        if sm == d:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open("input.txt", 'r')
    n = int(fptr.readline().strip())
    s = list(map(int, fptr.readline().rstrip().split()))
    first_multiple_input = fptr.readline().rstrip().split()
    d = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    result  = birthday(s, d, m)

    fptr.close()
    fptr = open("output.txt", 'w')
    fptr.write(str(result) + '\n')
    fptr.close()