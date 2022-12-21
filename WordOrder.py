# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
d = {}
for i in range(num):
    words = input() 
    if words in d:
        d[words] += 1
    else:
        d[words] = 1
print(len(d))
for k,v in d.items():
    print(v, end = " ")
