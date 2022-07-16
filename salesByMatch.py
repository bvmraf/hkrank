def sockMerchant(n, ar):
    pa = [0]*101
    spa = 0
    for i in range(n):
        pa[ar[i]] += 1
    for i in range(1, 101):
        spa += int(pa[i]/2)
    return spa
if __name__ == '__main__':
    f = open('input.txt','r')
    n = int(f.readline().rstrip())
    ar = list(map(int, f.readline().rstrip().split()))
    result = sockMerchant(n, ar)
    f.close()
    f = open('output.txt','w')
    f.write(str(result))
    f.close()