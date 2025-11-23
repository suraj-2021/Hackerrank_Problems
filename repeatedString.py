def repeatedString(s, n):
    s= [i for i in s]
    x = n//len(s)
    y = n % len(s)
    l = s.count('a')*x 
    l+=s[:y].count('a')
    return l
    
    if __name__ == '__main__':
    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)
    print(result)
