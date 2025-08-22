cube = lambda x: x**3

def fibonacci(N):
    m_list = []
    for i in range(N):
        if i == 0:
            m_list.append(0)
        elif i == 1:
            m_list.append(1)
        else:
            m_list.append(m_list[i-1] + m_list[i-2])
    return m_list
    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
