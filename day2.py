import sys

safeCount = 0
with open('day2.txt', 'r') as file:
    for line in file.read().splitlines():
        arr = line.strip().split()
        direction = 1 if int(arr[0]) < int(arr[1]) else -1
        isSafe = True
        for i in range(1, len(arr)):
            curr = int(arr[i])
            prev = int(arr[i-1])
            if curr >= prev:
                if direction == -1 or curr - prev > 3 or curr - prev < 1:
                    isSafe = False
                    break
            if curr < prev:
                if direction == 1 or prev - curr > 3 or prev - curr < 1:
                    isSafe = False
                    break
        if isSafe:
            safeCount += 1
print(safeCount)
