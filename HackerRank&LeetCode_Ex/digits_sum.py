import sys
for line in sys.stdin:
    temp = line.split(";")
    n = int(temp[1])
    lst = [int(x) for x in temp[0].split(",")]
    for i in range(len(lst)):
        if n - lst[i] in lst:
            print(str(lst[i]) + ","+str(n-lst[i]), end = ";")
            lst[i]=0
    break