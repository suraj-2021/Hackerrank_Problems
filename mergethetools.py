def merge_the_tools(string, k):
    substrings = []
    for i in range(0,len(string),k):
        x = string[i:k+i]
        s =""
        for j in x:
            if j not in s:
                s+=j
            else:
                continue
        substrings.append(s)
    print("\n".join(substrings))
               
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
