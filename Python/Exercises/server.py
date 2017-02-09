def server(tasks, n, T):
    total_time = 0
    for (i, t) in enumerate(tasks):
        if T < total_time + t:
            return i
        else:
            total_time += t
    return n

# Case number
c = 0

while True:
    c += 1
    try:
        entry = raw_input()
        n, T = entry.split(' ')
        n = int(n)
        T = int(T)
    except EOFError:
        break
    tasks = [int(t) for t in raw_input().split(' ')]
    print('Case {}: {}'.format(c, server(tasks, n, T)))
