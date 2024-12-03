import sys
import re

sum = 0
with open('day3sample.txt', 'r') as file:
    for line in file.read().splitlines():
        strings = re.findall(r"mul\(\d{1,3},\d{1,3}\)", line)
        for string in strings:
            x = string.split('(')[1].split(')')[0].split(',')
            x = int(x[0]) * int(x[1])
            sum += x
print(sum)

