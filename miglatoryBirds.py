def mingragoryBirds(arr):
    count = [0]*6
    for i in range(arr_count):
        count[arr[i]] += 1
    maxi = 1
    max = count[1]
    for i in range(2, 5):
        if max<count[i]:
            max = count[i]
            maxi = i
    return maxi
if __name__=='__main__':
    fptr = open("input.txt",'r')
    arr_count = int(fptr.readline().strip())
    arr = list(map(int, fptr.readline().rstrip().split()))
    result = mingragoryBirds(arr)

    fptr.close()
    fptr = open("output.txt",'w')
    fptr.write(str(result) + '\n')
    fptr.close()