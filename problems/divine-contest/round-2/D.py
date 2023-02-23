k = int(input())
boxes = [int(x) for x in input().split()]
print(sorted(boxes)[-k])