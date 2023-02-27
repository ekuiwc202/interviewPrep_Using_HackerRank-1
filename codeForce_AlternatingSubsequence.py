rep = int(input())
for i in range(rep):
    n = int(input())#
    arr = list(map(int, input().split()))
    
    sign = arr[0] // abs(arr[0])
    curElement = arr[0]
    curSum = 0
    
    for i in range(n):
        if sign != arr[i] // abs(arr[i]):
            curSum += curElement
            sign = -sign
            curElement =arr[i]
        
        curElement = max(arr[i], curElement)
    
    curSum += curElement
    
    print(curSum)
