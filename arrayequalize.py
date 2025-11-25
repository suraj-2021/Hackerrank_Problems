def equalizeArray(arr):
    counts = dict() 
    for i in arr:
        if i not in counts:
            counts[i]=1
        else:
            counts[i]+=1
    
    return(len(arr)-max(counts.values()))

if __name__ == '__main__':


    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)
    print(result)
