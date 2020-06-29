"""
Run an Merge Sort on the input file
"""
from readTxtFile import ReadFile
from OutputFile import output_file

# The name of the file we are reading from
data_file = 'data.txt'

# Get the items to sort from the read in file
items_to_sort = ReadFile(data_file)
items_to_sort = items_to_sort.get_contents()
print(items_to_sort)

# Separate the items b/c the first item is the number of items
sorted_arrays = []


def merge_sort(array, n):

    # Once the length of array has gotten to one, stop recurring
    if len(array) > 1:
        # Grab the middle element of the array
        if n % 2 == 0:
            mid = (n / 2) + 1
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


for array in items_to_sort:
    n = array[0]
    array = array[1::]
    sorted_array = merge_sort(array, n)
    sorted_arrays.append(sorted_array)

output_file('merge.out', sorted_arrays)
