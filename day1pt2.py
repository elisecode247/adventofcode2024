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
print(list1)
print(list2)
# similarity score by adding up each number in the left list
#  after multiplying it by the number of times that number appears in the right list.
score = 0
for x in range(0, len(list1)):
    score += list1[x] * list2.count(list1[x])
print(score)
