import sys
from functools import cmp_to_key

rules_done = False
rules = dict()
updates = []
sum = 0

def sortFunc(val1, val2):
  val1 = int(val1)
  val2 = int(val2)
  if val1 not in rules:
    return 1
  if val2 in rules[val1]:
     return -1
  if val1 in rules[val2]:
    return 1
  return 0

with open('day5.txt', 'r') as file:
    for line in file.read().splitlines():
        if (line == ''):
            rules_done = True
            continue
        if rules_done:
            updates.append(line.split(','))
        else:
            rule = line.split('|')
            if int(rule[0]) in rules:
                rules[int(rule[0])].append(int(rule[1]))
            else:
              rules[int(rule[0])] = [int(rule[1])]
    for update in updates:
        update_len = len(update)
        is_valid = True
        for i in range(0, len(update)):
            if i + 1 < update_len:
              curr = int(update[i])
              next = int(update[i+1])
              if curr not in rules or next not in rules[curr]:
                  is_valid = False
                  break
        if not is_valid:
            sorted_list = sorted(update, key=cmp_to_key(sortFunc))
            sum += int(sorted_list[(int((update_len - 1) / 2))])
    print(sum)
