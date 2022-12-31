n = int(input())
for i in range(n):
    a , b = input().split()
    a = int(a)
    val = input()
    val += val
    l = len(val)
    res = 0
    for i in range(len(val) - 1, -1, -1):
        if val[i] == "g":
            l = i
        if val[i] == b:
            res = max(res , l - i)
            
    print(res)
