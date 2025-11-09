import re

string = input()
pattern = input()

matches = re.finditer(f"(?=({pattern}))", string)
for match in matches:
    start = match.start()
    end = start + len(pattern) - 1
    print(f"({start}, {end})")
