from pathlib import Path
from collections import deque

def nested_list_contains(list_of_lists, target):
  for l in list_of_lists:
    for item in l:
      if target == item:
        return True
  return False


input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  numbers = list(map(int, input_file.read().splitlines()))

  # find first number that is not a sum of 2 of the previous 25 numbers
  answer = 0
  # build out initial sums of the first 25 numbers
  sums = []
  for idx, num1 in enumerate(numbers[:24]):
    sums.append([])
    for num2 in numbers[idx + 1:25]:
      sums[idx].append(num1 + num2)
  
  for idx, num1 in enumerate(numbers[25:]):
    num_idx = idx + 25
    if not nested_list_contains(sums, num1):
      answer = num1
      break
    # update the list of sums to use for the next iteration
    sums.pop(0)
    sums.append([])
    for sum_idx, num2 in enumerate(numbers[num_idx - 24:num_idx]):
      sums[sum_idx].append(num1 + num2)
  print(answer)
  
  # find contiguous numbers that sum to the number from part 1
  # return sum of smallest and largest addends
  addends = deque()
  for num in numbers:
    addends.append(num)
    while sum(addends) > answer:
      addends.popleft()
    if sum(addends) == answer:
      break
  sorted_addends = list(addends)
  sorted_addends.sort()
  print(sorted_addends[0] + sorted_addends[-1])
