"""
Run an Insertion Sort on the input file
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


def insert_sort(array, n):
    for j in range(1, n):
        key = array[j]
        i = j-1
        while i >= 0 and array[i] < key:
            array[i+1] = array[i]
            i = i - 1
        array[i+1] = key
    return array


for array in items_to_sort:
    n = array[0]
    array = array[1::]
    sorted_array = insert_sort(array, n)
    sorted_arrays.append(sorted_array)


output_file('insert.out', sorted_arrays)
