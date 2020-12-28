from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  lines = input_file.read().splitlines()

  # Find the number of valid passwords, based on count
  valid_passwords = 0
  for line in lines:
    count_range, letter, password = line.split(" ")
    count_min = int(count_range.split("-")[0])
    count_max = int(count_range.split("-")[1])
    count = 0
    for char in password:
      if char == letter[0]:
        count += 1
    if count >= count_min and count <= count_max:
      valid_passwords += 1
  print(valid_passwords)

  # Find the number of valid passwords, based on positions
  valid_passwords = 0
  for line in lines:
    indices, letter, password = line.split(" ")
    valid = False
    for index in indices.split("-"):
      if password[int(index) - 1] == letter[0]:
        valid = not valid
    if valid:
      valid_passwords += 1
  print(valid_passwords)
      

