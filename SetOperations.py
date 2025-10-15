class set_operations:
    def operations(self):
        n=int(input())
        numbers = set(list(map(int,input().split())))
        ni = int(input())
        for _ in range(ni):
            x = input().split()
            if len(x)==1 and len(numbers)>0:
                numbers.pop()
            if x[0]=='remove':
                try:
                   numbers.remove(int(x[1]))
                except KeyError:
                    pass
            if x[0]=='discard':
                numbers.discard(int(x[1]))
        print(sum(numbers))

p = set_operations()
p.operations()
