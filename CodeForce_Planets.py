from collections import Counter

Test_case = int(input())


for i in range(Test_case):
    l = list(input().split())
    planets = list(input().split())
    count_planets = Counter(planets)
    
    count = 0
    multiply = 0
    
    for v in count_planets.values():
        if v >= 2:
            multiply += int(l[1])
        else:
            count += 1

    print(multiply + count)
