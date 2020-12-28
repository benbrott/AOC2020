from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  rows = input_file.read().splitlines()
  row_length = len(rows[0])

  # Number of trees hit, right 3 down 1
  trees = 0
  index = 0
  for row in rows:
    if row[index] == "#":
      trees += 1
    index = (index + 3) % row_length
  print(trees)

  # Product of the number of trees hit:
  # Right 1, down 1
  # Right 3, down 1
  # Right 5, down 1
  # Right 7, down 1
  # Right 1, down 2
  product = 1
  for col_step, row_step in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    trees = 0
    row_index = 0
    col_index = 0
    for row_index in range(0, len(rows), row_step):
      if rows[row_index][col_index] == "#":
        trees += 1
      col_index = (col_index + col_step) % row_length
    product *= trees
  print(product)
      

