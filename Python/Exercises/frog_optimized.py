def solution(A, X, D):
    # Corner case
    if D >= X:
        return 0

    N = len(A)
    possible = [1 for i in xrange(D)] + [0 for i in xrange(X + 1 - D)]
    possible_sum = D

    for i in xrange(N):
        new = A[i]
        print new, possible
        max_reach = min(new+D, X)
        # Filling towards right
        for k in xrange(new, max_reach + 1):
            if possible[k]:
                continue
            else:
                possible[k] = 1
                possible_sum += 1
        if possible_sum == X+1:
            return i
    return -1