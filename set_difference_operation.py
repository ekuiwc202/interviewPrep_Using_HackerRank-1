E = int(input())
English_subscription = set(input().split())

F = int(input())
France_subscription = set(input().split())

print(len(English_subscription - France_subscription))
