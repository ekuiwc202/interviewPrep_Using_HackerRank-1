# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
def Task(n,blocks):
    left = 0
    right = len(blocks)-1
    k = "Yes"
    maximum = float('inf')
    while left < right:
       
        if blocks[right] <= blocks[left] and blocks[left] <= maximum :
            maximum = blocks[left]
            left += 1
        elif blocks[right] >= blocks[left] and blocks[right] <= maximum :
            maximum = blocks[right]
            right -= 1
        else:
            k = "No"
            break
    print(k)
for i in range(T):
    n = int(input())
    blocks = list(map(int,input().split()))
    Task(n,blocks)





