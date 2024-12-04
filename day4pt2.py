import sys
import re

grid = []

with open('day4.txt', 'r') as file:
    for line in file.read().splitlines():
        grid.append(list(line))

def mas_mas_count(grid):
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 'A':
        count += word_search(grid, r, c)
  return count

def word_search(grid, r, c):
  row_inbounds = 0 < r < len(grid) - 1
  col_inbounds = 0 < c < len(grid[0]) - 1
  if (not row_inbounds or not col_inbounds):
    return 0
  if ('M' in grid[r-1][c-1] and 'S' in grid[r-1][c+1] and 'M' in grid[r+1][c-1] and 'S' in grid[r+1][c+1]):
    return 1
  if ('S' in grid[r-1][c-1] and 'M' in grid[r-1][c+1] and 'S' in grid[r+1][c-1] and 'M' in grid[r+1][c+1]):
    return 1
  if ('S' in grid[r-1][c-1] and 'S' in grid[r-1][c+1] and 'M' in grid[r+1][c-1] and 'M' in grid[r+1][c+1]):
    return 1
  if ('M' in grid[r-1][c-1] and 'M' in grid[r-1][c+1] and 'S' in grid[r+1][c-1] and 'S' in grid[r+1][c+1]):
    return 1

  return 0

print(mas_mas_count(grid))
