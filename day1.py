import sys

list1, list2 = [], []

with open('sample1.txt', 'r') as file:
    for line in file.read().splitlines():
        arr = line.strip().split()
        list1.append(int(arr[0]))
        list2.append(int(arr[1]))

list1.sort()
list2.sort()

diffs = 0;
for x in range(len(list1)):
    diffs += abs(list1[x] - list2[x])

print(diffs)
