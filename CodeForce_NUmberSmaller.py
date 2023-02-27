n , m = list(map(int,input().split())) 
firstArray = list(map(int,input().split()))
secondArray = list(map(int,input().split()))
 
answer = []
 
pointer = 0
 
for i in range(m):
    while pointer  < n:
        if firstArray[pointer] < secondArray[i]:
            pointer += 1
        else:
            break
    answer.append(pointer)
print(*answer)
