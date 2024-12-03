import sys
import re

sum = 0
start = True
with open('day3.txt', 'r') as file:
    for line in file.read().splitlines():
        strings = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", line)

        for string in strings:
            if string == "do()":
                start = True
            elif string == "don't()":
                start = False
            elif start == True:
                x = string.split('(')[1].split(')')[0].split(',')
                x = int(x[0]) * int(x[1])
                sum += x
print(sum)

