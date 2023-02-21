from collections import defaultdict
Test_case = int(input())
for Test in range(Test_case):
    grid = []
    rows , cols = list(map(int,input().split()))
    for row in range(rows):
        grid.append(list(map(int,input().split())))
    index = []
    positive_diagonal = defaultdict(list)
    negative_diagonal = defaultdict(list)
    for row in range(rows):
        for col in range(cols):
            index.append((row,col))
    for row,col in index:
        positive_diagonal[row + col].append((row,col)) 
        negative_diagonal[row - col].append((row,col)) 
    for k, v in negative_diagonal.items():
        total = 0
        for row,col in v:
            total += grid[row][col]
        negative_diagonal[k]= total
    for k, v in positive_diagonal.items():
        total = 0
        for row,col in v:
            total += grid[row][col]
        positive_diagonal[k]= total
    max_result = 0
    for row,col in index:
        result = - grid[row][col]
        result += positive_diagonal[row + col]
        result += negative_diagonal[row - col]
        max_result = max(result,max_result)
    print(max_result)
