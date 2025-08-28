import re

n = int(input())
string = ""
for _ in range(n):
    string += input() + "\n"

def changer(match):
    if match.group() == "&&":
        return "and"
    else:
        return "or"

pattern = r"(?<=\s)(&&|\|\|)(?=\s)"

result = re.sub(pattern, changer, string)
print(result, end="")
