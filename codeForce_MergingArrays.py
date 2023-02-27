A , B = list(map(int,input().split())) 
Array_A = list(map(int,input().split()))
Array_B = list(map(int,input().split()))
 
pointer_A = 0
pointer_B = 0
answer = []
 
while pointer_A < A and pointer_B < B:
    if Array_A[pointer_A] < Array_B[pointer_B]:
        answer.append(Array_A[pointer_A])
        pointer_A += 1
    elif Array_A[pointer_A] > Array_B[pointer_B]:
        answer.append(Array_B[pointer_B])
        pointer_B += 1
    elif Array_A[pointer_A] == Array_B[pointer_B]:
        answer.append(Array_A[pointer_A])
        answer.append(Array_B[pointer_B])
        pointer_A += 1
        pointer_B += 1
while pointer_A < A:
    answer.append(Array_A[pointer_A])
    pointer_A += 1
while pointer_B < B:
    answer.append(Array_B[pointer_B])
    pointer_B += 1
print(*answer , sep = " ")
