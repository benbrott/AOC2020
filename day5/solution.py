from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  passes = input_file.read().splitlines()

  # Highest seat ID on a boarding pass
  max_seat = 0
  for boarding_pass in passes:
    min_row = 0
    max_row = 127
    for char in boarding_pass[:7]:
      half_rows = int((max_row + 1 - min_row) / 2)
      if char == "F":
        max_row -= half_rows
      elif char == "B":
        min_row += half_rows
    # min_row == max_row

    min_col = 0
    max_col = 7
    for char in boarding_pass[7:]:
      half_cols = int((max_col + 1 - min_col) / 2)
      if char == "L":
        max_col -= half_cols
      elif char == "R":
        min_col += half_cols
    # min_col == max_col

    seat_id = min_row * 8 + min_col
    if seat_id > max_seat:
      max_seat = seat_id
  print(max_seat)

  # My seat ID
  total_seats = 127 * 8 + 7
  seats_taken = [False] * total_seats
  min_seat = total_seats
  for boarding_pass in passes:
    min_row = 0
    max_row = 127
    for char in boarding_pass[:7]:
      half_rows = int((max_row + 1 - min_row) / 2)
      if char == "F":
        max_row -= half_rows
      elif char == "B":
        min_row += half_rows
    # min_row == max_row

    min_col = 0
    max_col = 7
    for char in boarding_pass[7:]:
      half_cols = int((max_col + 1 - min_col) / 2)
      if char == "L":
        max_col -= half_cols
      elif char == "R":
        min_col += half_cols
    # min_col == max_col

    seat_id = min_row * 8 + min_col
    seats_taken[seat_id] = True
    if seat_id < min_seat:
      min_seat = seat_id
  print(seats_taken.index(False, min_seat))
      

