# Enter your code here. Read input from STDIN. Print output to STDOUT

# build the individual possible ways in M step along dim d
def compute_individual(d, M):
    ways = [[0 for x in xrange(d)] for j in xrange(M)]
    # 1st step
    ways[0][0] = 1
    ways[0][-1] = 1
    for i in xrange(1, d-1):
        ways[0][i] = 2
    # Other steps
    for j in xrange(1, M):
        ways[j][0] = ways[j-1][1]
        ways[j][-1] = ways[j-1][-2]
        for i in xrange(1, d-1):
            ways[j][i] = ways[j-1][i + 1] + ways[j-1][i - 1]
    return ways

# Compute a lookup table, nCk = result[n][k]
def compute_k_n(N):
    result = [[0 for x in xrange(N+1)] for j in xrange(N+1)]
    result[0][0] = 1
    result[1][0] = 1
    result[1][1] = 1
    for n in xrange(2, N+1):
        for k in xrange(n+1):
            result[n][k] = result[n-1][k] + result[n-1][k-1]
    return result

# Compute along each dimension in D and return a dictionnary
def all_individual(D, M):
    ways = {}
    for i, d in enumerate(D):
        ways[i] = compute_individual(d, M)
    return ways

def compute_ways(X, D, M):
    if len(D) == 1:
        way = compute_individual(D[0], M)
        return way[M-1][X[0]]
    individual_ways = all_individual(D, M)
    if len(D) == 2:
        return
   
# Answer
T = int(raw_input())

for t in xrange(T):
    N, M = tuple([int(u) for u in raw_input().split()])
    X = [int(u) for u in raw_input().split()]
    D = [int(u) for u in raw_input().split()]
    print compute_k_n(5)