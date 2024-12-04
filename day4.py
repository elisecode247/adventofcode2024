import sys

grid = []

with open('day4.txt', 'r') as file:
    for line in file.read().splitlines():
        grid.append(list(line))

def xmas_count(grid):
  count = 0
  for r in range(len(grid)):
    for c in range(len(grid[0])):
      if grid[r][c] == 'X':
        left = word_search(grid, r, c - 1, 'M', 'left')
        right = word_search(grid, r, c + 1, 'M', 'right')
        up = word_search(grid, r - 1, c, 'M', 'up')
        down = word_search(grid, r + 1, c, 'M', 'down')
        diagonal_up_left = word_search(grid, r - 1, c - 1, 'M', 'upleft')
        diagonal_up_right = word_search(grid, r - 1, c + 1, 'M', 'upright')
        diagonal_down_left = word_search(grid, r + 1, c - 1, 'M', 'downleft')
        diagonal_down_right = word_search(grid, r + 1, c + 1, 'M', 'downright')
        count += left + right + up + down + diagonal_up_left + diagonal_up_right + diagonal_down_left + diagonal_down_right
  return count

def word_search(grid, r, c, char, direction):
  word = 'XMAS'
  row_inbounds = 0 <= r < len(grid)
  col_inbounds = 0 <= c < len(grid[0])
  if not row_inbounds or not col_inbounds:
    return 0
  if grid[r][c] != char:
    return 0
  if grid[r][c] == 'S':
    return 1
  next_char = word[word.index(char) + 1]
  if direction == 'left':
    return word_search(grid, r, c - 1, next_char, direction)
  elif direction == 'right':
    return word_search(grid, r, c + 1, next_char, direction)
  elif direction == 'up':
    return word_search(grid, r - 1, c, next_char, direction)
  elif direction == 'down':
    return word_search(grid, r + 1, c, next_char, direction)
  elif direction == 'upleft':
    return word_search(grid, r - 1, c - 1, next_char, direction)
  elif direction == 'upright':
    return word_search(grid, r - 1, c + 1, next_char, direction)
  elif direction == 'downleft':
    return word_search(grid, r + 1, c - 1, next_char, direction)
  elif direction == 'downright':
    return word_search(grid, r + 1, c + 1, next_char, direction)
  

print(xmas_count(grid)) # 18
