import sys
import re

sum = 0
text = ""
with open('day3 copy.txt', 'r') as file:
    for line in file.read().splitlines():
        text += line
strings = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", text)
start = True
for string in strings:
    if string == "do()":
        start = True
    elif string == "don't()":
        start = False
    elif start == True:
        x = string.split('(')[1].split(')')[0].split(',')
        x = int(x[0]) * int(x[1])
        sum += x
print(sum) # This time, the sum of the results is 48 (2*4 + 8*5).

