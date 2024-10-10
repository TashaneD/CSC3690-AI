# Hill climbing Algo based off graph in Hw

graph = {
    'A': ['B', 'C', 'U'],
    'B': ['E', 'G'],
    'C': ['G', 'I', 'J'],
    'E': ['G', 'M'],
    'G': ['M'],
    'I': ['M'],
    'J': ['K'],
    'K': ['J'],
    'U': ['K', 'Y'],
    'Y': ['M'],
    'M': []
}

# Heuristic values for each node
heuristics = {
    'A': 7,
    'B': 5,
    'C': 3,
    'U': 4,
    'E': 2,
    'G': 3,
    'I': 6,
    'J': 2,
    'K': 1,
    'Y': 2,
    'M': 0
}


def hill_climbing(graph, heuristics, start, goal):
    current_node = start
    path = [current_node]

    while current_node != goal:
        neighbors = graph[current_node]
        if not neighbors:
            print("There are no more neighbors to explore")
            return path

        # Gets the heurisitic value of each node
        def get_hvalue(node):
            return heuristics[node]

        # Find the neighbor with the lowest heuristic value
        next_node = min(neighbors, key=get_hvalue)

        # If the current node has a better or equal heuristic than the next node, cannot go any further
        if heuristics[next_node] >= heuristics[current_node]:
            print(f"Stuck at local optimum at node {current_node} with a heuristic value of {heuristics[current_node]}")
            return path

        # Move to the next node
        current_node = next_node
        path.append(current_node)

    return path

start_node = 'A'
goal_node = 'M'
path = hill_climbing(graph, heuristics, start_node, goal_node)

print("Path taken:",path)