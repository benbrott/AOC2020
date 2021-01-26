from pathlib import Path

def process_instruction(instruction):
  operation, number = instruction.split(" ")
  positive = number[0] == "+"
  value = int(number[1:])
  return (operation, positive, value)


# Execute until all of the instructions have been run or until an instruction is run a second time
def execute_instructions(instructions):
  num_instructions = len(instructions) 
  call_order = [None] * num_instructions
  counter = 1
  accumulator = 0
  index = 0
  did_complete = True
  while index < num_instructions:
    if call_order[index] is not None:
      did_complete = False
      break
    call_order[index] = counter
    counter += 1
    
    operation, positive, value = instructions[index]
    if operation == "nop":
      index += 1 
      continue
    if operation == "acc":
      if positive:
        accumulator += value
      else:
        accumulator -= value
      index += 1
    elif operation == "jmp":
      if positive:
        index += value
      else:
        index -= value
  return(accumulator, did_complete)


input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  instructions = list(map(process_instruction, input_file.read().splitlines()))
  
  # Accumulator value before an instruction is run a second time
  print(execute_instructions(instructions)[0])

  # Accumulator value at end of "patched" execution
  did_complete = False
  accumulator = 0
  patch_index = -1
  while not did_complete:
    patched_instructions = instructions.copy()
    while patch_index < len(patched_instructions):
      patch_index += 1
      operation, positive, value = patched_instructions[patch_index]
      if operation == "nop":
        patched_instructions[patch_index] = ("jmp", positive, value)
        break
      elif operation == "jmp":
        patched_instructions[patch_index] = ("nop", positive, value)
        break
    accumulator, did_complete = execute_instructions(patched_instructions)
  print(accumulator)
