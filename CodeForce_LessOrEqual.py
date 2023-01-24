n , k = list(map(int,input().split()))
num = list(map(int,input().split()))

num.sort()
if n == 1 and k == 0:
    if num[0] > 1:
        print(1)
    elif num[0] == 1:
        print(-1)
elif n > 1 and k == 0:
    if len(list(set(num))) < len(num) and num[0] > 1:
        print(num[0] - 1)
    elif num[0] > 1:
        print(num[0] - 1)
    else:
        print(-1)
elif k == n:
    print(num[-1])
elif k > 0:
    firstArray = num[:k]
    lastElement = firstArray[-1]
    secondArray = num[k:]
    
    if firstArray[-1] == secondArray[0]:
        print(-1)
    else:
        print(lastElement)
