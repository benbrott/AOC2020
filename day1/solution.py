from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  numbers = input_file.read().splitlines()

  # Find the 2 numbers that sum to 2020, print the product of them
  for idx, num1 in enumerate(numbers):
    for num2 in numbers[idx + 1:]:
      if int(num1) + int(num2) == 2020:
        print(int(num1) * int(num2))
  
  # Find the 3 numbers that sum to 2020, print the product of them
  for idx1, num1 in enumerate(numbers):
    for idx2, num2 in enumerate(numbers[idx1 + 1:], idx1 + 1):
      for num3 in numbers[idx2 + 1:]:
        if int(num1) + int(num2) + int(num3) == 2020:
          print(int(num1) * int(num2) * int(num3))

