import timeit
import sys
import itertools

# Import floyd_rec.py and floyd.py as modules
import floyd_rec
import floyd

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
def floyd_rec_perf():
    floyd_rec.floyd(graph)

elapsed_time_file1 = timeit.timeit(floyd_rec_perf, number=1)

# Performance test for file2.py
def floyd_perf():
    floyd.floyd(graph)

elapsed_time_file2 = timeit.timeit(floyd_perf, number=1)

# Print the results
print("Elapsed time for Floyd Algorithm using Recursion: {} seconds".format(elapsed_time_file1))
print("Elapsed time for Floyd Algorithm using Iteration: {} seconds".format(elapsed_time_file2))
