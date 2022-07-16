def countingValleys(steps, path):
    # Write your code here
    h = count = 0
    for i in range(steps):
        lh = h
        if path[i] == 'U':
            h += 1
        else:
            h -= 1
        if h >= 0 and lh < 0:
            count += 1
    return count
if __name__ == '__main__':
    fptr = open('input.txt', 'r')

    steps = int(fptr.readline().strip())

    path = fptr.readline()

    result = countingValleys(steps, path)
    print(result)

    fptr.close()