# Enter your code here. Read input from STDIN. Print output to STDOUT
A = set(input().split())
n = int(input())
def calculate(A,B):
    front = A - B
    back = B - A
    if not front  or back:
        return False
    return True

 
res = "True"
for i in range(n):
    B = set(input().split())
    if not calculate(A,B):
        res = "False"
        break

print(res)
