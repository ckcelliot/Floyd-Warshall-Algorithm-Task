import time
import sys
import itertools

# Import file1.py and file2.py as modules
import floyd_rec
import Geek4Geek

# Define the graph data for testing
NO_PATH = sys.maxsize
graph = [
    [0, 7, NO_PATH, 8],
    [NO_PATH, 0, 5, NO_PATH],
    [NO_PATH, NO_PATH, 0, 2],
    [NO_PATH, NO_PATH, NO_PATH, 0]
]
MAX_LENGTH = len(graph[0])

# Performance test for file1.py
start_time = time.time()

# Call the floyd function in file1.py to compute shortest path distances
floyd_rec.floyd(graph)

# Measure the time taken for the computation
end_time = time.time()
elapsed_time_file1 = end_time - start_time

# Performance test for file2.py
start_time = time.time()

# Call the floyd function in file2.py to compute shortest path distances
Geek4Geek.floydWarshall(graph)

# Measure the time taken for the computation
end_time = time.time()
elapsed_time_file2 = end_time - start_time

# Print the results
print("Elapsed time for Floyed Algorithm using Recursion: {} seconds".format(elapsed_time_file1))
print("Elapsed time for Floyed Algorithm from GeeksForGeeks: {} seconds".format(elapsed_time_file2))
