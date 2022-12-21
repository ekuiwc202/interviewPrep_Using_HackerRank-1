# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n = int(input())
room = Counter(list(map(int,input().split())))
for i in room:
    if room[i] == 1:
        print(i)
