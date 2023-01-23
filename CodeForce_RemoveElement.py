TestCase = int(input())
 
for i in range(TestCase):
    length = int(input())
    element = list(map(int,input().split()))
    element.sort()
    res = True
    
    for i in range(1,len(element)):
        if element[i] - element[i - 1] > 1:
            res = False
    if res == True:
        print("YES")
    else:
        print("NO")
        
