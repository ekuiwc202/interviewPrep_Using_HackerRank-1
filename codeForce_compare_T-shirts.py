T = int(input())
for test in range(T):
    compare1 , compare2 = input().split()
    if compare1[-1] != compare2[-1]:
        if compare1[-1] == "L":
            if compare2[-1] == "M" or compare2[-1] == "S":
                print(">")
        elif compare1[-1] == "M":
            if compare2[-1] == "S":
                print(">")
            else:
                print("<")
        elif compare1[-1] == "S":
            if compare2[-1] == "M" or compare2[-1] == "L":
                print("<")
    else:
        if len(compare1) == len(compare2):
                print("=")
        elif compare1[-1] == "L":
            if len(compare1) > len(compare2):
                print(">")
            else:
                print("<")
        elif compare1[-1] == "S":
            if len(compare1) > len(compare2):
                print("<")
            else:
                print(">")
