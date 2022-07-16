def bonAppetit(bill, k, b):
    ba = (sum(bill) - bill[k])/2
    if ba == b:
        print("Bon Appetit")
    else:
        print(b-ba)
if __name__ == "__main__":
    f = open("input.txt",'r')
    fmi = f.readline().rstrip().split()
    n = int(fmi[0])
    k = int(fmi[1])
    bill =  list(map(int, f.readline().rstrip().split()))
    b = int(f.readline().strip())
    f.close()
    bonAppetit(bill, k, b)
