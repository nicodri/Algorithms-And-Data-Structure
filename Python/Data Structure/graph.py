# Graph script
from collections import deque
from copy import deepcopy
import heapq

# Methods on Graph as adjacency list

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E']),
         'G': set(['H', 'I', 'J']),
         'H': set(['G']),
         'I': set(['G', 'J']),
         'J': set(['G', 'I'])}

# ## BFS:


def BFS_list(graph, start, visited=None):
    if visited is None:
        visited = set()
    current_component = set(start)
    visited.add(start)
    queue = deque(start)

    while queue:
        node = queue.popleft()
        for v in graph[node]:
            if v not in visited:
                visited.add(v)
                current_component.add(v)
                queue.append(v)
    return current_component


def shortest_path(graph, start, end):
    visited = set(start)
    queue = deque()
    queue.append((start, [start]))

    while queue:
        node, path = queue.popleft()
        for v in graph[node]:
            if v not in visited:
                visited.add(v)
                path = path + [v]
                if v == end:
                    return path
                queue.append((v, path))
    return []


def connected_components_bfs(graph):
    connected_components_list = []
    visited = set()
    for node in graph:
        if node not in visited:
            connected_components_list.append(BFS_list(graph, node, visited))
    return connected_components_list


# ## DFS

graph_directed = {'A': set(['B', 'C']),
                  'B': set(['D', 'E']),
                  'C': set(['E']),
                  'D': set(['E']),
                  'E': set([])}


def topological_ordering(graph):
    ordering = {}
    n = len(graph)

    graph = deepcopy(graph)
    return topological_ordering_(graph, ordering, n)


def topological_ordering_(graph, ordering, n):
    if n == 0:
        return ordering
    # Searching a sink vertex (always present in a DAG)
    sink_vertex = None
    for node in graph:
        if not graph[node]:
            # removing node from the graph
            graph.pop(node)
            for v in graph:
                if node in graph[v]:
                    graph[v].remove(node)
            sink_vertex = node
            break
    if sink_vertex is None:
        raise ValueError('Graph is not directed acyclic')
    ordering[sink_vertex] = n

    return topological_ordering_(graph, ordering, n-1)


def topological_ordering_dfs(graph):
    visited = set()
    ordering = {}
    n = len(graph)
    for node in graph:
        if node not in visited:
            ordering, n = topological_ordering_dfs_(node, graph, visited, ordering, n)
    return ordering


def topological_ordering_dfs_(node, graph, visited, ordering, n):
    visited.add(node)
    for v in graph[node]:
        if v not in visited:
            ordering, n = topological_ordering_dfs_(v, graph, visited, ordering, n)
    ordering[n] = node

    return ordering, n - 1


# ## Dijkstra (for connected graph)

graph = {'A': {'B': 7, 'C': 9, 'F': 14},
         'B': {'A': 7, 'C': 10, 'D': 15},
         'C': {'A': 9, 'B': 10, 'D': 11, 'F': 2},
         'D': {'B': 15, 'C': 11, 'E': 6},
         'E': {'D': 6, 'F': 9},
         'F': {'A': 14, 'C': 2, 'E': 9}}


def dijkstra_path(graph, start):
    # Maps each node to its distance to start
    path_weight = {node: float('inf') for node in graph}
    path_weight[start] = 0
    # Map from each node to its previous node in the current path
    previous = {}
    remaining = [(v, k) for k, v in path_weight.iteritems()]
    heapq.heapify(remaining)

    while len(remaining):
        kv = heapq.heappop(remaining)
        node = kv[1]
        for v in graph[node]:
            if path_weight[v] > path_weight[node] + graph[node][v]:
                path_weight[v] = path_weight[node] + graph[node][v]
                previous[v] = node
        # Rebuild heap (impossible to update a value with heapq module)
        remaining_list = []
        while remaining:
            kv = heapq.heappop(remaining)
            remaining_list.append(kv[1])
        remaining = [(path_weight[n], n) for n in remaining_list]
        heapq.heapify(remaining)
    return previous, path_weight


# ## MST problem

graph = {'A': {'B': 1, 'C': 5, 'D': 3},
         'B': {'A': 1, 'C': 4, 'D': 2},
         'C': {'A': 5, 'B': 4, 'D': 1},
         'D': {'A': 3, 'B': 2, 'C': 1}}


# Union Find structure
def build_unionfind(graph):
    parents = {}
    ranks = {}
    for node in graph:
        parents[node] = node
        ranks[node] = 0
    return parents, ranks


def find(node, parents):
    if parents[node] != node:
        node = find(parents[node], parents)
    return node


def union(group1, group2, parents, ranks):
    parent1 = find(group1, parents)
    parent2 = find(group2, parents)

    if parent1 != parent2:
        if ranks[parent1] > ranks[parent2]:
            parents[parent2] = parent1
            ranks[parent1] += ranks[parent2]
        else:
            parents[parent1] = parent2
            ranks[parent2] += ranks[parent1]
    return parents, ranks


def kruskals_naive(graph):
    # Sorting the edges in increasing order
    edges = []
    for k, v in graph.iteritems():
        for u, l in v.iteritems():
            edges.append((k, u, l))
    edges = list(set(edges))
    edges = sorted(edges, key=lambda x: x[2])

    parents, ranks = build_unionfind(graph)
    MST = set()
    for e in edges:
        a, b, l = e
        if find(a, parents) != find(b, parents):
            union(a, b, parents, ranks)
            MST.add(e)
    return MST






