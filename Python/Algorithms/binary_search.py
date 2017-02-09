
def loop_number(l):
    if l == 0:
        return 0
    elif l == 1:
        return 1
    elif l % 2 == 1:
        return l + 2 * loop_number((l-1) / 2)
    else:
        return l + loop_number(l / 2) + loop_number(l / 2 - 1)

# Cases counter
c = 0

while True:
    try:
        entry = raw_input()
    except EOFError:
        break
    for e in entry.split(' '):
        try:
            l = int(e)
        except ValueError:
            continue
        c += 1
        print 'Case {}: {}'.format(c, loop_number(l))
