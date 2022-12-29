from collections import defaultdict

T = int(input())

def Replace(n , to_be_Replaced , replaced):
        check = defaultdict(list)
        
        for (k , v) in zip(to_be_Replaced , replaced):
            check[k].append(v)
        
        res = "YES"
        for v in check.values():
            if len(set(v)) != 1:
                res  = "NO"
                break
                
        print(res)
for i in range(T):
    n = int(input())
    to_be_Replaced = list(input().split())
    replaced = list(input())
    Replace(n , to_be_Replaced , replaced)
