# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
d = defaultdict(list)
a, b = list(map(int, input().split()))
groupA = []
groupB = []
ans = []
for i in range(a):
    groupA.append(input())

for idx,val in enumerate(groupA):
    d[val].append(idx + 1)

for i in range(b):
    groupB.append(input())


for i in groupB:
    if i in d:
        ans.append(d[i])
    else:
        ans.append([-1])
    
for i in range(len(ans)):
    print(" ".join(str(e) for  e in ans[i]))
