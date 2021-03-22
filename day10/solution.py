from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  joltages = list(map(int, input_file.read().splitlines()))
  joltages.sort()
  joltages.insert(0, 0) # the initial joltage will always be 0
  joltages.insert(len(joltages), joltages[-1] + 3) # the adapter to the device will always have a 3-jolt difference

  # count differences of 1 and 3 jolts, return product
  one_diffs = 0
  three_diffs = 0
  prev = 0
  for joltage in joltages:
    diff = joltage - prev
    if (diff == 1):
      one_diffs += 1
    elif (diff == 3):
      three_diffs += 1
    prev = joltage
  print(one_diffs * three_diffs)

  # total valid combinations of adapters
  unique_paths = [(joltage, 0) for joltage in joltages]
  unique_paths[0] = (unique_paths[0][0], 1)
  for i in range(len(unique_paths)):
    joltage, paths = unique_paths[i]
    for j in range(i + 1, i + 4):
      if j < len(unique_paths) and unique_paths[j][0] - joltage <= 3:
        unique_paths[j] = (unique_paths[j][0], unique_paths[j][1] + paths)
  print(unique_paths[-1][1])
