from collections import Counter
 
n = int(input())
name = list(input().split())
bad = list(input().split())
 
k = []
count = 0
 
 
for i in range(len(name)):
    if len(set(name[i])) == len(name[i]) and name[i] not in bad:
        count += 1
print(count
