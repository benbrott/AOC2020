from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  directions = input_file.read().splitlines()
  compass = ['E', 'S', 'W', 'N']

  # Manhattan distance traveled
  facing = 'E'
  traveled = dict.fromkeys(compass , 0)
  for direction in directions:
    step = direction[0]
    value = int(direction[1:])
    if step == 'F':
      traveled[facing] = traveled[facing] + value
    elif step == 'R':
      index = compass.index(facing)
      facing = compass[(index + int(value / 90)) % 4]
    elif step == 'L':
      index = compass.index(facing)
      facing = compass[(index - int(value / 90)) % 4]
    else:
      traveled[step] = traveled[step] + value
  print(abs(traveled['E'] - traveled['W']) + abs(traveled['N'] - traveled['S']))

  # Manhattan distance traveled, with waypoint
  waypoint = {'E': 10, 'N': 1}
  traveled = {'E': 0, 'N': 0}
  for direction in directions:
    step = direction[0]
    value = int(direction[1:])
    if step == 'F':
      for key, distance in waypoint.items():
        traveled[key] = traveled[key] + distance * value
    elif step == 'R' or step == 'L':
      e, n = waypoint.values()
      if value == 180:
        waypoint = {'E': e * -1, 'N': n * -1}
        continue
      actual_step = step
      if value == 270:
        # convert the rotation_direction to now assume 90 degrees
        actual_step = 'L' if step == 'R' else 'R'
      if actual_step == 'R':
        waypoint = {'E': n, 'N': e * -1}
      else:
        waypoint = {'E': n * -1, 'N': e}
    else: # move the waypoint
      actual_step = step
      actual_value = value
      if step == 'W':
        actual_step = 'E'
        actual_value = -1 * actual_value
      elif step == 'S':
        actual_step = 'N'
        actual_value = -1 * actual_value
      waypoint[actual_step] = waypoint[actual_step] + actual_value
  print(abs(traveled['E'] + traveled['N']))
