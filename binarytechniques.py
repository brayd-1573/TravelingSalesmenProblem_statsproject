import random
import time
from scipy.stats import ttest_rel

def recursive_binary_search(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return recursive_binary_search(arr, target, low, mid - 1)
    else:
        return recursive_binary_search(arr, target, mid + 1, high)

def iterative_binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1

def measure_runtimes(search_function, arr, target, num_searches):
    runtimes = []
    if search_function == recursive_binary_search:
        for i in range(num_searches):
            start_time = time.time()
            search_function(arr, target, 0, len(arr)-1)
            end_time = time.time()
            runtimes.append(end_time - start_time)
        print("Recursive runtimes: " ,runtimes)
        return runtimes
    else:
         for i in range(num_searches):
            start_time = time.time()
            search_function(arr, target)
            end_time = time.time()
            runtimes.append(end_time - start_time)
         print("Iterative runtimes: " ,runtimes)
         return runtimes

# Generate a sorted list of integers to search
arr = sorted([random.randint(0, 1000) for i in range(100)])

# Define the target value to search for
target = 42

# Measure the runtimes of recursive and iterative binary search
num_searches = 30
recursive_runtimes = measure_runtimes(recursive_binary_search, arr, target, num_searches)
iterative_runtimes = measure_runtimes(iterative_binary_search, arr, target, num_searches)

# Compare the runtimes of recursive and iterative binary search
stat, pvalue = ttest_rel(recursive_runtimes, iterative_runtimes)
if pvalue < 0.05:
    print("The difference in runtime is statistically significant.")
else:
    print("The difference in runtime is not statistically significant.")
