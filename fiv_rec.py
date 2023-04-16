import sys

NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])

def floyd_recursive(distance, intermediate, start_node, end_node):
    """
    A tail-recursive implementation of Floyd's algorithm
    """
    if start_node == MAX_LENGTH:
        return

    if end_node == MAX_LENGTH:
        return floyd_recursive(distance, intermediate, start_node + 1, 0)

    if start_node == end_node:
        distance[start_node][end_node] = 0
        return floyd_recursive(distance, intermediate, start_node, end_node + 1)

    # Update distance using intermediate node
    distance[start_node][end_node] = min(
        distance[start_node][end_node],
        distance[start_node][intermediate] + distance[intermediate][end_node]
    )

    return floyd_recursive(distance, intermediate, start_node, end_node + 1)

def floyd(distance):
    """
    Wrapper function for tail-recursive implementation of Floyd's algorithm
    """
    for intermediate in range(MAX_LENGTH):
        floyd_recursive(distance, intermediate, 0, 0)

# Call the function to compute shortest path distances
floyd(graph)

# Print the resulting shortest path distances
print(graph)
