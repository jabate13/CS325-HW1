"""
Run an Insertion Sort on the input file
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


# The actual insertion sort
@timer
def insert_sort(array, n):
    for j in range(1, n):
        key = array[j]
        i = j-1
        while i >= 0 and array[i] < key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key
    return array


# Output to the console
print('Timer for 5000:')
insert_sort(rand_5000, 5000)
print('Timer for 10000:')
insert_sort(rand_10000, 10000)
print('Timer for 15000:')
insert_sort(rand_15000, 15000)
print('Timer for 20000:')
insert_sort(rand_20000, 20000)
print('Timer for 30000:')
insert_sort(rand_30000, 30000)
print('Timer for 40000:')
insert_sort(rand_40000, 40000)
print('Timer for 50000:')
insert_sort(rand_50000, 50000)
print('Timer for 100000:')
insert_sort(rand_100000, 100000)
