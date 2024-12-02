import sys
arr = [];
with open('day1.txt', 'r') as f:
    while True:
        line = f.readline()
        arr.append(line.strip().split())
        if not line:
            break
list1 = []
list2 = []
for x in range(0, len(arr) - 1):
    list1.append(int(arr[x][0]))
    list2.append(int(arr[x][1]))
list1.sort()
list2.sort()

diffs = 0;
for x in range(0, len(list1)):
    diffs += abs(list1[x] - list2[x])
print(diffs)
