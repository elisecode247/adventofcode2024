import sys

safeCount = 0
def processLine(line, skipIndex = -1):
    newArr = line.copy()
    if (skipIndex >= len(line)):
        return False
    if skipIndex > -1:
        newArr.pop(skipIndex)
    direction = 1 if int(newArr[0]) < int(newArr[1]) else -1
    isSafe = True
    for i in range(1, len(newArr)):
        curr = int(newArr[i])
        prev = int(newArr[i-1])
        if curr >= prev:
            if direction == -1 or curr - prev > 3 or curr - prev < 1:
                isSafe = False
                break
        if curr < prev:
            if direction == 1 or prev - curr > 3 or prev - curr < 1:
                isSafe = False
                break
    if isSafe == False and skipIndex < len(line):
        return processLine(arr, skipIndex + 1)
    elif isSafe == False and skipIndex == len(line):
        return False
    else:
        return True


with open('day2.txt', 'r') as file:
    for line in file.read().splitlines():
        arr = line.strip().split()
        isSafe = processLine(arr, -1)
        if isSafe:
            safeCount += 1
print(safeCount)
