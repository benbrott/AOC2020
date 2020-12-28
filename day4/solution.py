from pathlib import Path
import re

input_path = Path(__file__).parent / "input.txt"
with input_path.open() as input_file:
  passports = input_file.read().split("\n\n")

  # Number of valid passports, by present fields
  valid_passports = 0
  for passport in passports:
    has_info = [False] * 7
    for key_value in passport.replace("\n", " ").split(" "):
      if key_value == "":
        continue
      key = key_value.split(":")[0]
      if key == "byr":
        has_info[0] = True
      elif key == "iyr":
        has_info[1] = True
      elif key == "eyr":
        has_info[2] = True
      elif key == "hgt":
        has_info[3] = True
      elif key == "hcl":
        has_info[4] = True
      elif key == "ecl":
        has_info[5] = True
      elif key == "pid":
        has_info[6] = True
    if False not in has_info:
      valid_passports += 1
  print(valid_passports)

  # Number of valid passports, by validated fields
  valid_passports = 0
  for passport in passports:
    valid_info = [False] * 7
    for key_value in passport.replace("\n", " ").split(" "):
      if key_value == "":
        continue
      key, value = key_value.split(":")
      if key == "byr":
        if int(value) >= 1920 and int(value) <= 2002:
          valid_info[0] = True
      elif key == "iyr":
        if int(value) >= 2010 and int(value) <= 2020:
          valid_info[1] = True
      elif key == "eyr":
        if int(value) >= 2020 and int(value) <= 2030:
          valid_info[2] = True
      elif key == "hgt":
        if "cm" not in value and "in" not in value:
          continue
        val, unit = value.replace("cm", " cm").replace("in", " in").split(" ")
        if (unit == "cm" and int(val) >= 150 and int(val) <= 193) or (unit == "in" and int(val) >= 59 and int(val) <= 76):
          valid_info[3] = True
      elif key == "hcl":
        if re.search(r'^#[0-9a-f]{6}$', value):
          valid_info[4] = True
      elif key == "ecl":
        if value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
          valid_info[5] = True
      elif key == "pid":
        if len(value) == 9:
          valid_info[6] = True
    if False not in valid_info:
      valid_passports += 1
  print(valid_passports)
      

