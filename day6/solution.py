from pathlib import Path

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  groups = input_file.read().split("\n\n")

  # Total yes answers by group
  total = 0
  for group in groups:
    individual_answers = group.split("\n")
    group_answers = set(individual_answers[0])
    for answers in individual_answers[1:]:
      group_answers.update(answers)
    total += len(group_answers)
  print(total)

  # Total yes answers by group (intersection)
  total = 0
  for group in groups:
    individual_answers = group.split("\n")
    group_answers = set(individual_answers[0])
    for answers in individual_answers[1:]:
      if answers != "":
        group_answers.intersection_update(answers)
    total += len(group_answers)
  print(total)
      

