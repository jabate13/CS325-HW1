"""
Run an Merge Sort on the input file
"""
from random import randint
from time import time


def create_random_array(n):

    # Initialize the container array
    rand_array = []

    # Fill the array with random ints between 0 and 10,000
    for i in range(n):
        rand_array.append(randint(0, 10000))

    return rand_array


# Create the random arrays
rand_5000 = create_random_array(5000)
rand_10000 = create_random_array(10000)
rand_15000 = create_random_array(15000)
rand_20000 = create_random_array(20000)
rand_30000 = create_random_array(30000)
rand_40000 = create_random_array(40000)
rand_50000 = create_random_array(50000)
rand_100000 = create_random_array(100000)

# A decorator to add to the merge to print out the time it takes to execute
def timer(method):

    def timed(*args, **kw):
        # get the start time
        start_time = time()
        # Run the function
        result = method(*args, **kw)
        # Get the end time
        end_time = time()

        # Print the runtime by subtracting end/start times
        print(str((end_time - start_time) * 1000) + 'ms')
        return result
    return timed

# A function that runs the merge_sort (so the decorator doesn't run a million times with recursion
@timer
def merge_runner(array, n):
    merge_sort(array, n)


def merge_sort(array, n):

    # Once the length of array has gotten to one, stop recurring
    if len(array) > 1:
        # Grab the middle element of the array

        mid = n // 2
        n = n // 2
        # Break the array into two parts at midpoint
        left_array = array[:mid]
        right_array = array[mid:]
        # Set the left/right arrays = recursive mergesort
        left_array = merge_sort(left_array, len(left_array))
        right_array = merge_sort(right_array, len(right_array))

        # Re-Initialize the array
        array = []

        # Actually start the merging
        while len(left_array) > 0 and len(right_array) > 0:
            # Look at the first values for each array and grab the bigger one. Add that bigger value to the array
            if left_array[0] < right_array[0]:
                array.append(right_array[0])
                right_array.pop(0)
            else:
                array.append(left_array[0])
                left_array.pop(0)

        # Append the remaining values to the array
        for i in left_array:
            array.append(i)
        for i in right_array:
            array.append(i)

    return array


# Output to the console
print('Timer for 5000:')
merge_runner(rand_5000, 5000)
print('Timer for 10000:')
merge_runner(rand_10000, 10000)
print('Timer for 15000:')
merge_runner(rand_15000, 15000)
print('Timer for 20000:')
merge_runner(rand_20000, 20000)
print('Timer for 30000:')
merge_runner(rand_30000, 30000)
print('Timer for 40000:')
merge_runner(rand_40000, 40000)
print('Timer for 50000:')
merge_runner(rand_50000, 50000)
print('Timer for 10000:')
merge_runner(rand_100000, 100000)


