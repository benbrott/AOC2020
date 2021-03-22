from pathlib import Path

def get_occupied_adjacent_seats(seats, i, j):
  occupied = 0
  for x in range(i - 1, i + 2):
    if x < 0 or x >= len(seats): continue
    for y in range(j - 1, j + 2):
      if y < 0 or y >= len(seats[0]): continue
      if x == i and y == j: continue
      if seats[x][y] == "#": occupied += 1
  return occupied


def get_occupied_visible_seats(seats, i, j):
  occupied = 0
  directions = [
    (0, -1), # left
    (1, -1),
    (1, 0), # down
    (1, 1),
    (0, 1), # right
    (-1, 1),
    (-1, 0), # up
    (-1, -1)
  ]
  for di, dj in directions:
    seat = "."
    x = i
    y = j
    while seat == ".":
      x = x + di
      y = y + dj
      if x < 0 or x >= len(seats) or y < 0 or y >= len(seats[0]): break
      seat = seats[x][y]
    if seat == "#": occupied += 1    
  return occupied


input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  og_seats = [list(line) for line in input_file.read().splitlines()]

  # number of occupied seats after the seats stabilize
  seats = [row[:] for row in og_seats]
  while True:
    seats_to_change = []
    for i, seat_row in enumerate(seats):
      for j, seat in enumerate(seat_row):
        if seats[i][j] == ".":
          continue
        occupied = get_occupied_adjacent_seats(seats, i, j)
        if seat == "L" and occupied == 0:
          seats_to_change.append((i, j))
        elif seat == "#" and occupied >= 4:
          seats_to_change.append((i, j))
    if len(seats_to_change) == 0:
      break
    for i, j in seats_to_change:
      if seats[i][j] == "L":
        seats[i][j] = "#"
      else:
        seats[i][j] = "L"
  
  occupied = 0
  for seat_row in seats:
    for seat in seat_row:
      if seat == "#":
        occupied += 1
  print(occupied)

  # number of occupied seats after the seats stabilize (visibility, not adjacency)
  seats = [row[:] for row in og_seats]
  while True:
    seats_to_change = []
    for i, seat_row in enumerate(seats):
      for j, seat in enumerate(seat_row):
        if seats[i][j] == ".":
          continue
        occupied = get_occupied_visible_seats(seats, i, j)
        if seat == "L" and occupied == 0:
          seats_to_change.append((i, j))
        elif seat == "#" and occupied >= 5:
          seats_to_change.append((i, j))
    if len(seats_to_change) == 0:
      break
    for i, j in seats_to_change:
      if seats[i][j] == "L":
        seats[i][j] = "#"
      else:
        seats[i][j] = "L"
  
  occupied = 0
  for seat_row in seats:
    for seat in seat_row:
      if seat == "#":
        occupied += 1
  print(occupied)
