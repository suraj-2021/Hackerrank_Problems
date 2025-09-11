import re

def wrapper(func):
    def fun(l):
        formatted_numbers = []
        for number in l:
            match = re.search(r'(\d{10})$', number)
            if match:
                ten_digit_num = match.group(1)
                formatted_numbers.append(f'+91 {ten_digit_num[:5]} {ten_digit_num[5:]}')
        
        func(sorted(formatted_numbers))
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


