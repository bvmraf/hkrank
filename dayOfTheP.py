def dop(year):
    if year == 1918:
        day = '26.09.'
    else:
        if year < 1918:
            if year%4 == 0:
                day = '12.09.'
            else:
                day = '13.09.'
        else:
            if year%400 == 0:
                day = '12.09.'
            elif (year%4 == 0 and year%100 != 0):    
                day = '12.09.'
            else:
                day = '13.09.'
    return day+str(year)
if __name__=='__main__':
    fptr = open("input.txt",'r')
    year = int(fptr.read())
    result = dop(year)
    fptr.close()
    fptr = open("output.txt",'w')
    fptr.write(result)
    fptr.close()