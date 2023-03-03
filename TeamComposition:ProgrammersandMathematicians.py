TestCase = int(input())
for i in range(TestCase):
    a, b = list(map(int,input().split()))
    left , right = -1 , (a+b)//4 + 1
    while left + 1 < right:
        mid = left + (right - left)// 2
        if mid <= min(a, b):
            left = mid
        else:
            right = mid
    print(left)
