import re
for _ in range(int(input())):
    x = input()
    check_length = False
    check_uppercase = False
    check_digits = False
    check_repeats = False

    if len(re.findall(r"[A-Z]",x))>=2:
        check_uppercase = True 
    if len(x)==10:
        check_length = True
    if len(re.findall(r"[0-9]",x))>=3:
        check_digits = True
    if len(x) == len(set(x)):
        check_repeats = True
        
    if check_length and check_uppercase and check_digits and check_repeats:
        print("Valid")
    else:
        print("Invalid")
