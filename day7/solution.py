from pathlib import Path

def bag_could_contain(bag, target, bags_contained):
  bag_colors = [bag_info[1] for bag_info in bags_contained[bag]]
  if target in bag_colors:
    return True
  for container in bag_colors:
    if bag_could_contain(container, target, bags_contained):
      return True
  return False


def total_bags_contained(bag, bags_contained):
  total = 1
  for bag_count, bag_color in bags_contained[bag]:
    total += bag_count * total_bags_contained(bag_color, bags_contained)
  return total


input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  rules = input_file.read().replace(".", "").splitlines()
  bags_contained = dict()
  for rule in rules:
    bag_color, contents_text = rule.split(" bags contain ")
    bags_contained[bag_color] = []
    if not contents_text.startswith("no "):
      for content_text in contents_text.split(", "):
        content_info = content_text.split(" ")
        content_count = int(content_info[0])
        content_color = " ".join(content_info[1:-1])
        bags_contained[bag_color].append((content_count, content_color))
  
  # Bags that could contain shiny gold
  total = 0
  for container in bags_contained:
    if bag_could_contain(container, "shiny gold", bags_contained):
      total += 1
  print(total)

  # Bags inside shiny gold (-1 to remove the shiny gold bag itself)
  print(total_bags_contained("shiny gold", bags_contained) - 1)

